#!/usr/bin/env python
#
# Collectd plugin for apache-solr
#

import sys
import re
import urllib2
import collections
import collectd
import json

DEFAULT_INTERVAL = 10
DEFAULT_API_TIMEOUT = 60
PLUGIN_NAME = 'solr'
VERBOSE_LOGGING = True

Metric = collections.namedtuple('Metric', ('name', 'type'))

CORE_METRICS = {
    'SEARCHER.searcher.deletedDocs':
        Metric('solr.core_deleted_docs', 'counter'),
    'SEARCHER.searcher.indexVersion':
        Metric('solr.core_indexed_docs', 'counter'),
    'SEARCHER.searcher.numDocs':
        Metric('solr.core_num_docs', 'counter'),
    'CORE.fs.totalSpace':
        Metric('solr.core_totalspace', 'gauge'),
    'CORE.fs.usableSpace':
        Metric('solr.core_usablespace', 'gauge'),
    'INDEX.sizeInBytes':
        Metric('solr.core_index_size', 'gauge'),
    'CACHE.searcher.documentCache.cumulative_hitratio':
        Metric('solr.document_cache_cumulative_hitratio', 'gauge'),
    'CACHE.searcher.fieldValueCache.cumulative_hitratio':
        Metric('solr.field_value_cache_cumulative_hitratio', 'gauge'),
    'CACHE.searcher.queryResultCache.cumulative_hitratio':
        Metric('solr.query_result_cache_cumulative_hitratio', 'gauge')
}

NODE_METRICS = {
    'node': {
        'ADMIN./admin/collections.requestTimes.mean_ms':
            Metric('solr.node.collections.requestTimes', 'gauge'),
        'ADMIN./admin/cores.requestTimes.mean_ms':
            Metric('solr.node.cores.requestTimes', 'gauge'),
        'ADMIN./admin/zookeeper.requestTimes.mean_ms':
            Metric('solr.node.zookeeper.requestTimes', 'gauge'),
    },
    'jetty': {
        'DefaultHandler.2xx-responses.count':
            Metric('solr.http_2xx_responses', 'counter'),
        'DefaultHandler.4xx-responses.count':
            Metric('solr.http_4xx_responses', 'counter'),
        'DefaultHandler.requests.count':
            Metric('solr.http_requests', 'counter'),
        'DefaultHandler.requests.mean_ms':
            Metric('solr.jetty_request_latency', 'gauge')
    },
    'jvm': {
        'memory.heap.usage':
            Metric('solr.jvm_heap_usage', 'gauge'),
        'buffers.direct.MemoryUsed':
            Metric('solr.jvm_direct_memory_used', 'gauge'),
        'buffers.direct.TotalCapacity':
            Metric('solr.jvm_direct_memory_capacity', 'gauge'),
        'memory.total.max':
            Metric('solr.jvm_total_memory', 'gauge'),
        'memory.total.used':
            Metric('solr.jvm_total_memory_used', 'gauge'),
        'memory.pools.Metaspace.usage':
            Metric('solr.jvm.memory.pools.Metaspace.usage', 'gauge'),
        'memory.pools.Par-Eden-Space.usage':
            Metric('solr.jvm.memory.pools.Par-Eden-Space.usage', 'gauge'),
        'memory.pools.Par-Survivor-Space.usage':
            Metric('solr.jvm.memory.pools.Par-Survivor-Space.usage', 'gauge'),
        'memory.pools.Code-Cache.usage':
            Metric('solr.jvm.memory.pools.Code-Cache.usage', 'gauge'),
        'gc.ConcurrentMarkSweep.count':
            Metric('solr.jvm_gc_cms_count', 'gauge'),
        'gc.ConcurrentMarkSweep.time':
            Metric('solr.jvm_gc_cms_time', 'gauge'),
        'gc.ParNew.count':
            Metric('solr.jvm_gc_parnew_count', 'gauge'),
        'gc.ParNew.time':
            Metric('solr.jvm_gc_parnew_time', 'gauge'),
        'threads.count':
            Metric('solr.jvm_active_threads', 'gauge'),
        'threads.runnable.count':
            Metric('solr.jvm_runnable_threads', 'gauge')
    }
}


def log_verbose(msg):
    if not VERBOSE_LOGGING:
        return
    collectd.info('solr_info plugin [verbose]: %s' % msg)


def configure_callback(conf):
    """Receive configuration block"""
    plugin_conf = {}
    cluster = ''
    interval = DEFAULT_INTERVAL
    custom_dimensions = {}
    enhanced_metrics = False
    exclude_optional_metrics = set()
    include_optional_metrics = set()
    http_timeout = DEFAULT_API_TIMEOUT

    required_keys = frozenset(('Host', 'Port'))

    for val in conf.children:
        if val.key in required_keys:
            plugin_conf[val.key] = val.values[0]
        elif val.key == 'Interval' and val.values[0]:
            interval = val.values[0]
        elif val.key == 'Cluster' and val.values[0]:
            cluster = val.values[0]
            custom_dimensions['cluster'] = val.values[0]
        elif val.key == 'Dimension':
            if len(val.values) == 2:
                custom_dimensions.update({val.values[0]: val.values[1]})
            else:
                collectd.warning("WARNING: Check configuration setting for %s" % val.key)
        elif val.key == 'EnhancedMetrics' and val.values[0]:
            enhanced_metrics = str_to_bool(val.values[0])
        elif val.key == 'IncludeMetric' and val.values[0]:
            include_optional_metrics.add(val.values[0])
        elif val.key == 'ExcludeMetric' and val.values[0]:
            exclude_optional_metrics.add(val.values[0])

    collectd.debug("Configuration settings:")

    for key in required_keys:
        try:
            val = plugin_conf[key]
            collectd.debug("%s : %s" % (key, val))
        except KeyError:
            raise KeyError("Missing required config setting: %s" % key)

    base_url = ("http://%s:%s/solr" % (plugin_conf['Host'], plugin_conf['Port']))

    module_config = {
        'state': None,
        'member_id': ("%s:%s" % (
            plugin_conf['Host'], plugin_conf['Port'])),
        'plugin_conf': plugin_conf,
        'cluster': cluster,
        'interval': interval,
        'base_url': base_url,
        'port': plugin_conf['Port'],
        'http_timeout': http_timeout,
        'custom_dimensions': custom_dimensions,
        'enhanced_metrics': enhanced_metrics,
        'include_optional_metrics': include_optional_metrics,
        'exclude_optional_metrics': exclude_optional_metrics,
    }

    collectd.debug("module_config: (%s)" % str(module_config))

    collectd.register_read(
        read_metrics,
        data=module_config,
        name=module_config['member_id'])


def read_metrics(data):
    log_verbose('solr plugin: Read callback called')
    solrCloud = fetch_collections_info(data)
    default_dimensions = data['custom_dimensions']

    response = fetch_solr_stats(data)
    if response is None:
        return

    solr_metrics = flatten_dict(response)
    dispatch_core_stats(data, solr_metrics, default_dimensions, solrCloud)
    dispatch_node_stats(data, solr_metrics, default_dimensions, solrCloud)


def str_to_bool(flag):
    """Converts true/false to boolean"""
    flag = str(flag).strip().lower()
    if flag == 'true':
        return True
    elif flag != 'false':
        collectd.warning("WARNING: REQUIRES BOOLEAN. \
                RECEIVED %s. ASSUMING FALSE." % (str(flag)))

    return False


def parse_corename(core):
    core = re.sub(r'_', '.', core)
    return core


def dispatch_value(instance, key, value, value_type, dimensions=None):
    """Dispatch a value to collectd"""
    # log_verbose('Sending value: %s.%s=%s' % (instance, key, value))
    val = collectd.Values(plugin=PLUGIN_NAME)
    val.plugin_instance = instance

    dim_str = get_dimension_string(dimensions)
    if dim_str:
        val.plugin_instance += '[{dims}]'.format(dims=dim_str)

    val.type = value_type
    val.type_instance = key
    val.values = [value]
    val.meta = {'0': True}

    log_verbose('Emitting value: %s' % val)
    val.dispatch()


def get_dimension_string(dimensions):
    dim_str = ''
    if dimensions:
        dim_str = ','.join(['='.join(d) for d in dimensions.items()])

    return dim_str


def prepare_dimensions(default_dimensions, core, solrCloud=None, collection=None):
    dimensions = default_dimensions

    if 'error' in solrCloud.keys():
        dimensions['core'] = core
    else:
        dimensions['collection'] = collection
        dimensions['node'] = solrCloud[collection]['node']
        dimensions['shard'] = solrCloud[collection]['shard']
        dimensions['core'] = solrCloud[collection]['core']

    return dimensions


def get_cores(data):
    url = '%s/admin/cores?action=status&wt=json' % data['base_url']
    cores = []
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        json_data = json.loads(f.read())
        cores = json_data['status'].keys()
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info, HTTP error: ' + str(e.code))
        log_verbose(url)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info: ' + str(e.reason))
        log_verbose(url)

    return cores


def fetch_solr_stats(data):
    """Connect to Solr stat page and and return JSON object"""
    url = '%s/admin/metrics?wt=json&type=all&group=all' % (data['base_url'])

    if data['cluster'] is not None and 'leader' not in data.keys():
        log_verbose('Ignore metrics for solrCloud replica node %s' % data['base_url'])
        return None
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        json_data = json.loads(f.read())
        return json_data
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info, HTTP error: ' + str(e.code))
        log_verbose(url)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info: ' + str(e.reason))
        log_verbose(url)

    return None


def fetch_collections_info(data):
    """Connect to SolrCloud status page and and return JSON object"""
    url = '%s/admin/collections?action=CLUSTERSTATUS&wt=json' % data['base_url']
    get_data = None
    solrCloud = {}
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        get_data = json.loads(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ')
        solrCloud['error'] = 'Solr instance is not running in SolrCloud mode'
        return solrCloud
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)

    if 'error' in get_data.keys():
        log_verbose('%s' % get_data['error']['msg'])
        solrCloud['error'] = get_data['error']['msg']
    elif 'cluster' in get_data.keys():
        log_verbose('Solr running in SolrCloud mode')
        solrCollections = get_data['cluster']['collections'].keys()
        leader_url = 'http://172.31.45.252:' + data['port'] + '/solr'
        # solrCloud['leader'] = False

        for collection in solrCollections:
            solrShards = get_data['cluster']['collections'][collection]['shards']
            for shard in solrShards.keys():
                for coreNodes in solrShards[shard]['replicas'].keys():
                    coreNode = solrShards[shard]['replicas'][coreNodes]
                    if 'leader' in coreNode.keys() and coreNode['base_url'] == leader_url:
                        # and coreNode['base_url'] == data['base_url']
                        solrCloud[collection] = {}
                        log_verbose('leader node %s' % coreNode['node_name'])
                        data['leader'] = True
                        solrCloud[collection]['leader'] = coreNode['leader']
                        solrCloud[collection]['core'] = coreNode['core']
                        solrCloud[collection]['node'] = coreNode['node_name']
                        solrCloud[collection]['shard'] = shard
                        solrCloud[collection]['collection'] = collection
    return solrCloud


def flatten_dict(d, result=None):
    """
    flatten_dict method will take a nested 'dict' as a parameter and
    converts it to a single nested dict by merging all the nested keys
    to a single key with '.' using recursion.
    """
    if result is None:
        result = {}
    for key in d:
        value = d[key]
        if isinstance(value, dict):
            value1 = {}
            for keyIn in value:
                value1[".".join([key, keyIn])] = value[keyIn]
            flatten_dict(value1, result)
        elif isinstance(value, (list, tuple)):
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    index = 0
                    for keyIn in element:
                        newkey = ".".join([key, keyIn])
                        value1[newkey] = value[indexB][keyIn]
                        index += 1
                    for keyA in value1:
                        flatten_dict(value1, result)
                elif isinstance(element, list):
                    if len(element) == 2:
                        keyB = ".".join([key, str(element[0])])
                        keyB = keyB.replace(".value", "")
                        result[keyB] = element[1]
        else:
            key = key.replace(".value", "")
            result[key] = value
    return result


def dispatch_core_stats(data, solr_metrics, default_dimensions, solrCloud):
    plugin_instance = data['member_id']
    cores = get_cores(data) if 'error' in solrCloud.keys() else None

    for key in solrCloud.keys() if cores is None else cores:
        core = parse_corename(solrCloud[key]['core']) if cores is None else key
        log_verbose('collection: {0}'.format(key))
        for cmetric in CORE_METRICS.keys():
            metric = "metrics.solr.core.{0}.{1}".format(core, cmetric)
            if metric in solr_metrics.keys():
                dimensions = prepare_dimensions(default_dimensions, core, solrCloud, key)
                dispatch_value(
                    plugin_instance,
                    CORE_METRICS[cmetric].name,
                    solr_metrics[metric],
                    CORE_METRICS[cmetric].type,
                    dimensions
                )


def dispatch_node_stats(data, solr_metrics, default_dimensions, solrCloud):
    plugin_instance = data['member_id']
    core = None
    collection = None

    if 'error' not in solrCloud.keys():
        for key in solrCloud.keys():
            if data['member_id']+'_solr' == solrCloud[key]['node']:
                collection = key
                core = solrCloud[key]['core']

    for registry in ('node', 'jetty', 'jvm'):
        for nmetric in NODE_METRICS[registry].keys():
            if registry == 'jetty':
                metric = "metrics.solr.jetty.org.eclipse.jetty.server.handler.{0}".format(nmetric)
            else:
                metric = "metrics.solr.{0}.{1}".format(registry, nmetric)
            if metric in solr_metrics.keys():
                dimensions = prepare_dimensions(default_dimensions, core, solrCloud, collection)
                dispatch_value(
                    plugin_instance,
                    NODE_METRICS[registry][nmetric].name,
                    solr_metrics[metric],
                    NODE_METRICS[registry][nmetric].type,
                    dimensions
                )


if __name__ == "__main__":
    # run standalone
    pass
else:
    collectd.register_config(configure_callback)
