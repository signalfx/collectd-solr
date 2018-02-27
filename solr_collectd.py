#!/usr/bin/env python

import urllib2
import urllib_ssl_handler
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
        Metric('solr.core_deleted_docs', 'gauge'),
    'SEARCHER.searcher.maxDoc':
        Metric('solr.core_max_docs', 'gauge'),
    'SEARCHER.searcher.numDocs':
        Metric('solr.core_num_docs', 'gauge'),
    'SEARCHER.searcher.warmupTime':
        Metric('solr.searcher_warmup', 'gauge'),
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
        Metric('solr.query_result_cache_cumulative_hitratio', 'gauge'),
    'QUERY./select.requestTimes.mean_ms':
        Metric('solr.search_query_response', 'gauge'),
    'QUERY./select.requests.count':
        Metric('solr.search_query_requests', 'counter'),
    'REPLICATION./replication.requestTimes.mean_ms':
        Metric('solr.replication_handler_response', 'gauge'),
    'REPLICATION./replication.requests.count':
        Metric('solr.replication_handler_requests', 'counter'),
    'UPDATE./update.requestTimes.mean_ms':
        Metric('solr.update_request_handler_response', 'gauge'),
    'UPDATE./update.requests.count':
        Metric('solr.update_handler_requests', 'counter')
}

NODE_METRICS = {
    'node': {
        'ADMIN./admin/collections.requests.count':
            Metric('solr.node_collections_requests', 'counter'),
        'ADMIN./admin/cores.requests.count':
            Metric('solr.node_cores_requests', 'counter'),
        'ADMIN./admin/zookeeper.requests.count':
            Metric('solr.node_zookeeper_requests', 'counter'),
        'ADMIN./admin/metrics.requests.count':
            Metric('solr.node_metrics_requests', 'counter')
    },
    'jetty': {
        'DefaultHandler.2xx-responses.count':
            Metric('solr.http_2xx_responses', 'counter'),
        'DefaultHandler.4xx-responses.count':
            Metric('solr.http_4xx_responses', 'counter'),
        'DefaultHandler.5xx-responses.count':
            Metric('solr.http_5xx_responses', 'counter'),
        'DefaultHandler.requests.count':
            Metric('solr.http_requests', 'counter'),
        'DefaultHandler.requests.mean_ms':
            Metric('solr.jetty_request_latency', 'gauge')
    },
    'jvm': {
        'memory.heap.usage':
            Metric('solr.jvm_heap_usage', 'gauge'),
        'memory.total.max':
            Metric('solr.jvm_total_memory', 'gauge'),
        'memory.total.used':
            Metric('solr.jvm_total_memory_used', 'gauge'),
        'memory.pools.Metaspace.usage':
            Metric('solr.jvm_memory_pools_Metaspace_usage', 'gauge'),
        'memory.pools.Par-Eden-Space.usage':
            Metric('solr.jvm_memory_pools_Par-Eden-Space_usage', 'gauge'),
        'memory.pools.Par-Survivor-Space.usage':
            Metric('solr.jvm_memory_pools_Par-Survivor-Space_usage', 'gauge'),
        'memory.pools.Code-Cache.usage':
            Metric('solr.jvm_memory_pools_Code-Cache_usage', 'gauge'),
        'gc.ConcurrentMarkSweep.count':
            Metric('solr.jvm_gc_cms_count', 'gauge'),
        'gc.ConcurrentMarkSweep.time':
            Metric('solr.jvm_gc_cms_time', 'gauge'),
        'gc.ParNew.count':
            Metric('solr.jvm_gc_parnew_count', 'gauge'),
        'gc.ParNew.time':
            Metric('solr.jvm_gc_parnew_time', 'gauge')
    }
}

ENHANCED_METRICS = {
    'metrics.solr.jetty.org.eclipse.jetty.server.handler.DefaultHandler.active-requests.count':
        Metric('solr.http_active_requests', 'gauge'),
    'metrics.solr.jetty.org.eclipse.jetty.server.handler.DefaultHandler.get-requests.mean_ms':
        Metric('solr.jetty_get_request_latency', 'gauge'),
    'metrics.solr.jetty.org.eclipse.jetty.server.handler.DefaultHandler.post-requests.mean_ms':
        Metric('solr.jetty_post_request_latency', 'gauge'),
    'metrics.solr.node.ADMIN./admin/zookeeper.requestTimes.mean_ms':
        Metric('solr.zookeeper_request_time', 'gauge'),
    'metrics.solr.node.ADMIN./admin/metrics.requestTimes.mean_ms':
        Metric('solr.node_metric_request_time', 'gauge'),
    'metrics.solr.node.ADMIN./admin/metrics.requests.count':
        Metric('solr.node_metric_request_count', 'counter'),
    'metrics.solr.node.ADMIN./admin/zookeeper.errors.count':
        Metric('solr.zookeeper_errors', 'counter'),
    'metrics.solr.jvm.os.openFileDescriptorCount':
        Metric('solr.jvm_open_filedescriptors', 'counter'),
    'metrics.solr.jvm.classes.loaded':
        Metric('solr.jvm_classes_loaded', 'counter'),
    'metrics.solr.jvm.buffers.mapped.MemoryUsed':
        Metric('solr.jvm_mapped_memory_used', 'gauge'),
    'metrics.solr.jvm.buffers.mapped.TotalCapacity':
        Metric('solr.jvm_mapped_memory_capacity', 'gauge')
}


def make_logger_name(member_id):
    return "%s.%s" % (PLUGIN_NAME, member_id)


def configure_callback(conf):
    """Receive configuration block"""
    plugin_conf = {}
    cluster = 'default'
    interval = DEFAULT_INTERVAL
    username = None
    password = None
    custom_dimensions = {}
    enhanced_metrics = False
    exclude_optional_metrics = set()
    include_optional_metrics = set()
    ssl_keys = {}
    http_timeout = DEFAULT_API_TIMEOUT
    testing = False

    required_keys = frozenset(('Host', 'Port'))

    for val in conf.children:
        if val.key in required_keys:
            plugin_conf[val.key] = val.values[0]
        elif val.key == 'Username' and val.values[0]:
            username = val.values[0]
        elif val.key == 'Password' and val.values[0]:
            password = val.values[0]
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
        elif val.key == 'ssl_keyfile' and val.values[0]:
            ssl_keys['ssl_keyfile'] = val.values[0]
        elif val.key == 'ssl_certificate' and val.values[0]:
            ssl_keys['ssl_certificate'] = val.values[0]
        elif val.key == 'ssl_ca_certs' and val.values[0]:
            ssl_keys['ssl_ca_certs'] = val.values[0]
        elif val.key == 'Testing' and val.values[0]:
            testing = str_to_bool(val.values[0])

    for key in required_keys:
        try:
            val = plugin_conf[key]
        except KeyError:
            raise KeyError("Missing required config setting: %s" % key)

    base_url = ("http://{0}:{1}/solr".format(plugin_conf['Host'], plugin_conf['Port']))

    https_handler = None
    if 'ssl_certificate' in ssl_keys and 'ssl_keyfile' in ssl_keys:
        base_url = ('https' + base_url[4:])
        https_handler = urllib_ssl_handler.HTTPSHandler(key_file=ssl_keys['ssl_keyfile'],
                                                        cert_file=ssl_keys['ssl_certificate'],
                                                        ca_certs=ssl_keys['ssl_ca_certs'])

    # Auth handler to handle basic http authentication.
    auth = urllib2.HTTPPasswordMgrWithDefaultRealm()
    if username is None and password is None:
        username = password = ''

    auth.add_password(None, uri=base_url, user=username, passwd=password)
    auth_handler = urllib2.HTTPBasicAuthHandler(auth)
    if https_handler:
        opener = urllib2.build_opener(auth_handler, https_handler)
    else:
        opener = urllib2.build_opener(auth_handler)

    module_config = {
        'state': None,
        'member_id': ("{0}:{1}".format(
            plugin_conf['Host'], plugin_conf['Port'])),
        'plugin_conf': plugin_conf,
        'cluster': cluster,
        'interval': interval,
        'ssl_keys': ssl_keys,
        'base_url': base_url,
        'opener': opener,
        'username': username,
        'password': password,
        'http_timeout': http_timeout,
        'custom_dimensions': custom_dimensions,
        'enhanced_metrics': enhanced_metrics,
        'include_optional_metrics': include_optional_metrics,
        'exclude_optional_metrics': exclude_optional_metrics,
    }

    if testing:
        return module_config

    collectd.register_read(
        read_metrics,
        data=module_config,
        name=module_config['member_id'])


def read_metrics(data):
    solr_cloud = fetch_collections_info(data)
    if not solr_cloud:
        return None

    default_dimensions = data['custom_dimensions']
    collectd.debug("{0} - STARTED FETCHING METRICS".format(data['member_id']))
    if data['member_id']+'_solr' == get_leader_node(data):
        for collection in solr_cloud.keys():
            response = get_shards_info(data, collection) if collection is not 'live_nodes' else None
            if response is not None:
                dispatch_collection_stats(data, response, default_dimensions, solr_cloud, collection)

    response = fetch_solr_stats(data)
    if response is None:
        return None

    solr_metrics = flatten_dict(response)
    dispatch_core_stats(data, solr_metrics, default_dimensions, solr_cloud)
    dispatch_node_stats(data, solr_metrics, default_dimensions)

    if data['enhanced_metrics'] or len(data['include_optional_metrics']) > 0:
        dispatch_additional_metrics(data, solr_metrics, default_dimensions)


def str_to_bool(flag):
    """Converts true/false to boolean"""
    flag = str(flag).strip().lower()
    if flag == 'true':
        return True
    elif flag != 'false':
        collectd.warning("WARNING: REQUIRES BOOLEAN. \
                RECEIVED %s. ASSUMING FALSE." % (str(flag)))

    return False


def dispatch_value(instance, key, value, value_type, dimensions=None):
    """Dispatch a value to collectd"""
    val = collectd.Values(plugin=PLUGIN_NAME)
    val.plugin_instance = instance

    dim_str = get_dimension_string(dimensions)
    if dim_str:
        val.plugin_instance += '[{dims}]'.format(dims=dim_str)

    val.type = value_type
    val.type_instance = key
    val.values = [value]
    val.meta = {'0': True}
    val.dispatch()


def get_dimension_string(dimensions):
    dim_str = ''
    if dimensions:
        dim_str = ','.join(['='.join(d) for d in dimensions.items()])

    return dim_str


def prepare_dimensions(default_dimensions, core=None, solr_cloud=None, collection=None, shard=None):
    if len(locals()) == 1:
        return default_dimensions

    dimensions = default_dimensions
    if 'error' in solr_cloud.keys() and core is not None:
        dimensions['core'] = core
    elif solr_cloud and collection:
        dimensions['collection'] = collection
        dimensions['shard'] = shard
        dimensions['core'] = core
        dimensions['node'] = solr_cloud[collection][shard][core]['node']
        dimensions['leader'] = solr_cloud[collection][shard][core]['leader']

    return dimensions


def _api_call(url, opener=None):
    """
    _api_call will handle all the calls to the api.
    It adds http basic authentication header if provided.
    The response of the api call is then deserialized from json to dict.
    """
    resp = None
    collectd.debug("METRICS FROM %s ENDPOINT" % url)
    try:
        if opener is not None:
            urllib2.install_opener(opener)
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
    except (urllib2.HTTPError, urllib2.URLError) as e:
        collectd.error("Error making API call ({0}) {1}".format(e, url))
        return None
    try:
        return json.load(resp)
    except ValueError as e:
        collectd.error("Error parsing JSON for API call ({0}) {1}".format(e, url))
        return None


def get_cores(data):
    url = '{0}/admin/cores?action=status&wt=json'.format(data['base_url'])

    return _api_call(url, data['opener'])['status'].keys()


def fetch_solr_stats(data):
    """Connect to Solr stat page and and return JSON object"""
    url = '{0}/admin/metrics?wt=json&type=all&group=all'.format(data['base_url'])

    return _api_call(url, data['opener'])


def get_shards_info(data, collection):
    url = '{0}/{1}/select?q=*:*&shards.info=true&wt=json'.format(data['base_url'], collection)

    return _api_call(url, data['opener'])


def get_leader_node(data):
    url = '{0}/admin/collections?action=OVERSEERSTATUS&wt=json'.format(data['base_url'])
    response = _api_call(url, data['opener'])

    return response['leader']


def fetch_collections_info(data):
    """Connect to solr_cloud status page and and return JSON object"""
    url = '{0}/admin/collections?action=CLUSTERSTATUS&wt=json'.format(data['base_url'])
    get_data = _api_call(url, data['opener'])
    solr_cloud = {}

    if get_data is None:
        collectd.error('solr_collectd plugin: can\'t get info')
        solr_cloud['error'] = 'Solr instance is not running in solr_cloud mode'
    elif 'error' in get_data.keys():
        collectd.warning('%s' % get_data['error']['msg'])
        solr_cloud['error'] = get_data['error']['msg']
    elif 'cluster' in get_data.keys():
        if 'cluster' not in data['custom_dimensions']:
            data['custom_dimensions']['cluster'] = data['cluster']
        solr_cloud['live_nodes'] = get_data['cluster']['live_nodes']
        solrCollections = get_data['cluster']['collections'].keys()
        for collection in solrCollections:
            solr_cloud[collection] = {}
            solrShards = get_data['cluster']['collections'][collection]['shards']
            for shard in solrShards.keys():
                solr_cloud[collection][shard] = {}
                for coreNodes in solrShards[shard]['replicas'].keys():
                    coreNode = solrShards[shard]['replicas'][coreNodes]
                    core = coreNode['core']
                    solr_cloud[collection][shard][core] = {}
                    # if 'leader' in coreNode.keys() and coreNode['base_url'] == data['base_url']:
                    #     collectd.debug('{0} - Solr running in solr_cloud mode'.format(data['member_id']))
                    solr_cloud[collection][shard][core]['node'] = coreNode['node_name']
                    solr_cloud[collection][shard][core]['base_url'] = coreNode['base_url']
                    if 'leader' in coreNode.keys():
                        solr_cloud[collection][shard][core]['leader'] = coreNode['leader']
                    else:
                        solr_cloud[collection][shard][core]['leader'] = 'false'
    return solr_cloud


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


def dispatch_additional_metrics(data, solr_metrics, default_dimensions):
    plugin_instance = data['member_id']
    dpm_count = 0
    default_dimensions['node'] = data['member_id'] + '_solr'

    if data['enhanced_metrics']:
        for metric in ENHANCED_METRICS.keys():
            if metric in data['exclude_optional_metrics']:
                continue
            if metric in solr_metrics.keys():
                dispatch_value(
                    plugin_instance,
                    ENHANCED_METRICS[metric].name,
                    solr_metrics[metric],
                    ENHANCED_METRICS[metric].type,
                    default_dimensions
                )
                dpm_count += 1
    else:
        for metric in data['include_optional_metrics']:
            if metric in solr_metrics.keys():
                dispatch_value(plugin_instance, metric, solr_metrics[metric], 'gauge', default_dimensions)
                dpm_count += 1
    return dpm_count


def parse_shard_info(shards_info, shard):
    shard += '_'
    for key in shards_info['shards.info'].keys():
        if shard in key:
            num_doc = shards_info['shards.info'][key]['numFound']
            core = shards_info['shards.info'][key]['shardAddress'].split("/")[4]
            return num_doc, core


def parse_corename(collection, shard, core_val):
    replica = core_val.split("_")[-1]
    core = "{0}.{1}.{2}".format(collection, shard, replica)

    return core


def dispatch_collection_stats(data, shards_info, default_dimensions, solr_cloud, collection):
    plugin_instance = data['member_id']
    metric_name = 'solr.shard_cumulative_docs'
    for shard in solr_cloud[collection].keys():
        num_doc, core = parse_shard_info(shards_info, shard)
        dimensions = prepare_dimensions(default_dimensions, core, solr_cloud, collection, shard)
        dispatch_value(plugin_instance, metric_name, num_doc, 'gauge', dimensions)


def dispatch_core_stats(data, solr_metrics, default_dimensions, solr_cloud):
    plugin_instance = data['member_id']
    dpm_count = 0
    cores = get_cores(data) if 'error' in solr_cloud.keys() else None

    for key in solr_cloud.keys() if cores is None else cores:
        if key is 'live_nodes':
            continue
        for shard in solr_cloud[key].keys():
            for core_val in solr_cloud[key][shard].keys():
                core = parse_corename(key, shard, core_val) if cores is None else key
                for cmetric in CORE_METRICS.keys():
                    metric = "metrics.solr.core.{0}.{1}".format(core, cmetric)
                    if metric in data['exclude_optional_metrics']:
                        continue
                    if metric in solr_metrics.keys():
                        dimensions = prepare_dimensions(
                            default_dimensions, core_val, solr_cloud, key, shard)
                        dispatch_value(
                            plugin_instance,
                            CORE_METRICS[cmetric].name,
                            solr_metrics[metric],
                            CORE_METRICS[cmetric].type,
                            dimensions
                        )
                        dpm_count += 1
    return dpm_count


def dispatch_node_stats(data, solr_metrics, default_dimensions):
    plugin_instance = data['member_id']
    dpm_count = 0
    default_dimensions['node'] = data['member_id']+'_solr'

    for registry in ('node', 'jetty', 'jvm'):
        for nmetric in NODE_METRICS[registry].keys():
            if registry == 'jetty':
                metric = "metrics.solr.jetty.org.eclipse.jetty.server.handler.{0}".format(nmetric)
            else:
                metric = "metrics.solr.{0}.{1}".format(registry, nmetric)
            if metric in data['exclude_optional_metrics']:
                continue
            if metric in solr_metrics.keys():
                dispatch_value(
                    plugin_instance,
                    NODE_METRICS[registry][nmetric].name,
                    solr_metrics[metric],
                    NODE_METRICS[registry][nmetric].type,
                    default_dimensions
                )
                dpm_count += 1
    return dpm_count


if __name__ == "__main__":
    # run standalone
    pass
else:
    collectd.register_config(configure_callback)
