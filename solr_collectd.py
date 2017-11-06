#!/usr/bin/env python
#
# Collectd plugin for apache-solr
#

import sys
import re
import urllib2
import collectd
import json

try:
    import xml.etree.cElementTree as etree
except ImportError:
    try:
        import xml.etree.ElementTree as etree
    except ImportError:
        print 'python >= 2.5'
        sys.exit()

DEFAULT_INTERVAL = 10
DEFAULT_API_TIMEOUT = 60
PLUGIN_NAME = "solr"
VERBOSE_LOGGING = True

CORE_SELF_METRICS = [
    "numDocs",
    "maxDoc",
    "deletedDocs",
    "indexHeapUsageBytes"
]

CORE_GAUGE_METRICS = [
    "CORE.fs.totalSpace",
    "CORE.fs.usableSpace",
    "INDEX.sizeInBytes",
    "UPDATE.updateHandler.adds",
    "UPDATE.updateHandler.errors",
    "UPDATE.updateHandler.deletesById",
    "UPDATE.updateHandler.deletesByQuery",
    "ADMIN.luke.requestTimes",
    "ADMIN.ping.requestTimes",
    "ADMIN.system.requestTimes",
    "QUERY.browse.requestTimes",
    "QUERY.get.requestTimes",
    "QUERY.requestTimes",
    "QUERY.select.requestTimes",
    "REPLICATION.requestTimes",
    "REPLICATION.time",
    "SEARCHER.new.time",
    "SEARCHER.new.warmup",
    "UPDATE.requestTimes",
    "ADMIN.system.errors",
    "QUERY.errors",
    "REPLICATION.errors",
    "UPDATE.errors",
    "UPDATE.updateHandler.commits",
    "UPDATE.updateHandler.cumulativeAdds",
    "UPDATE.updateHandler.cumulativeDeletesById",
    "UPDATE.updateHandler.cumulativeDeletesByQuery",
    "UPDATE.updateHandler.cumulativeErrors"
]

NODE_GAUGE_METRICS = [
    "CONTAINER.cores.loaded",
    "CONTAINER.cores.lazy",
    "CONTAINER.fs.totalSpace",
    "CONTAINER.fs.usableSpace",
    "QUERY.httpShardHandler.availableConnections",
    "QUERY.httpShardHandler.maxConnections",
    "UPDATE.updateShardHandler.availableConnections",
    "UPDATE.updateShardHandler.maxConnections",
    "ADMIN.collections.requestTimes",
    "ADMIN.cores.requestTimes",
    "ADMIN.metrics.requestTimes",
    "ADMIN.zookeeper.requestTimes",
    "CONTAINER.threadPool.coreContainerWorkExecutor.duration",
    "CONTAINER.threadPool.coreLoadExecutor.duration",
    "QUERY.httpShardHandler.threadPool.httpShardExecutor.duration",
    "UPDATE.updateShardHandler.threadPool.updateExecutor.duration",
    "ADMIN.collections.errors",
    "ADMIN.cores.errors",
    "ADMIN.metrics.errors",
    "ADMIN.zookeeper.errors",
    "CONTAINER.threadPool.coreContainerWorkExecutor.completed",
    "CONTAINER.threadPool.coreLoadExecutor.completed",
    "QUERY.httpShardHandler.threadPool.httpShardExecutor.completed",
    "UPDATE.updateShardHandler.threadPool.updateExecutor.completed"
]

JVM_GAUGE_METRICS = [
    "buffers.mapped.used",
    "classes.loaded",
    "classes.unloaded",
    "memory.heap.used",
    "memory.heap.usage",
    "memory.total.max",
    "memory.total.used",
    "os.AvailableProcessors",
    "os.FreePhysicalMemorySize",
    "os.FreeSwapSpaceSize",
    "os.ProcessCpuLoad",
    "os.SystemLoadAverage",
    "os.TotalPhysicalMemorySize",
    "threads.blocked.count",
    "threads.count",
    "threads.runnable.count",
    "threads.waiting.count"
]

JETTY_GAUGE_METRICS = [
    "server.handler.DefaultHandler.percent-4xx-1m",
    "server.handler.DefaultHandler.percent-5xx-1m",
    "util.thread.QueuedThreadPool.qtp225493257.utilization",
    "util.thread.QueuedThreadPool.qtp225493257.utilization-max",
    "server.handler.DefaultHandler.connect-requests",
    "server.handler.DefaultHandler.delete-requests",
    "server.handler.DefaultHandler.dispatches",
    "server.handler.DefaultHandler.get-requests",
    "server.handler.DefaultHandler.post-requests",
    "server.handler.DefaultHandler.requests",
    "server.handler.DefaultHandler.2xx-responses",
    "server.handler.DefaultHandler.4xx-responses"
]

CORE_COUNTER_METRICS = [
    "ADMIN.file.requests",
    "ADMIN.luke.requests",
    "ADMIN.mbeans.requests",
    "ADMIN.ping.requests",
    "ADMIN.system.requests",
    "QUERY.browse.requests",
    "QUERY.get.requests",
    "QUERY.requests",
    "QUERY.stream.requests",
    "REPLICATION.requests",
    "SEARCHER.new",
    "SEARCHER.new.errors",
    "SEARCHER.new.maxReached",
    "UPDATE.requests"
]

NODE_COUNTER_METRICS = [
    "ADMIN.collections.requests",
    "ADMIN.cores.requests",
    "ADMIN.metrics.requests",
    "ADMIN.zookeeper.requests"
]

JETTY_COUNTER_METRICS = [
    "server.handler.DefaultHandler.active-dispatches",
    "server.handler.DefaultHandler.active-requests",
    "server.handler.DefaultHandler.active-suspended"
]


def log_verbose(msg):
    if not VERBOSE_LOGGING:
        return
    collectd.info('solr_info plugin [verbose]: %s' % msg)


def configure_callback(conf):
    """Receive configuration block"""
    plugin_conf = {}
    cluster = 'default'
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
        elif val.key == 'Dimension':
            if len(val.values) == 2:
                custom_dimensions.update({val.values[0]: val.values[1]})
            else:
                collectd.warning("WARNING: Check configuration \
                                                setting for %s" % val.key)
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

    base_url = ("http://%s:%s" % (plugin_conf['Host'], plugin_conf['Port']))

    module_config = {
        'state': None,
        'member_id': ("%s:%s" % (
            plugin_conf['Host'], plugin_conf['Port'])),
        'plugin_conf': plugin_conf,
        'cluster': cluster,
        'interval': interval,
        'base_url': base_url,
        'http_timeout': http_timeout,
        'custom_dimensions': custom_dimensions,
        'enhanced_metrics': enhanced_metrics,
        'include_optional_metrics': include_optional_metrics,
        'exclude_optional_metrics': exclude_optional_metrics,
    }

    collectd.debug("module_config: (%s)" % str(module_config))

    collectd.register_read(
        read_callback,
        data=module_config,
        name=module_config['member_id'])


def str_to_bool(flag):
    """Converts true/false to boolean"""
    flag = str(flag).strip().lower()
    if flag == 'true':
        return True
    elif flag != 'false':
        collectd.warning("WARNING: REQUIRES BOOLEAN. \
                RECEIVED %s. ASSUMING FALSE." % (str(flag)))

    return False


def parse_mtsname(mts_name):
    """Remove any slash (/) chars and duplicate attribute names"""
    mts_name = re.sub(r'(\.http://)', '.', mts_name)
    mts_name = re.sub(r'(\./|/)', '.', mts_name)
    mts_name = re.sub(r'ADMIN\.admin\.', 'ADMIN.', mts_name)
    mts_name = re.sub(r'QUERY\.query\.', 'QUERY.', mts_name)
    mts_name = re.sub(r'UPDATE\.update\.', 'UPDATE.', mts_name)
    mts_name = re.sub(r'REPLICATION\.replication\.', 'REPLICATION.', mts_name)
    mts_name = re.sub(r'org\.eclipse\.jetty\.', '', mts_name)
    return mts_name


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

    # log_verbose('Emitting value: %s' % val)
    val.dispatch()


def get_dimension_string(dimensions):
    dim_str = ''
    if dimensions:
        dim_str = ','.join(['='.join(d) for d in dimensions.items()])

    return dim_str


def dispatch_core_counter_metrics(plugin_instance, cores_map, solr_metrics, default_dimensions):
    """Extract required gauge metrics and dispatch to collectd"""
    for solrMetric in solr_metrics.findall('./lst/lst'):
        metric_name = solrMetric.attrib['name'].strip()
        core = re.sub(r'solr\.core\.', '', metric_name)
        core = re.sub(r'\.', '_', core)
        dimensions = prepare_dimensions(default_dimensions, core, cores_map)
        for solrMts in solrMetric.findall('./lst'):
            mts_name = solrMts.attrib['name'].strip()
            mts_name = parse_mtsname(mts_name)
            if mts_name in CORE_COUNTER_METRICS:
                mts_val = solrMts[0].text
                dispatch_value(plugin_instance, mts_name, mts_val, 'counter', dimensions)


def dispatch_counter_metrics(plugin_instance, solr_metrics, cores_map):
    """Extract required counter metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        mts_name = parse_mtsname(mts_name)
        if any(mts_name in l for l in (NODE_COUNTER_METRICS, JETTY_COUNTER_METRICS)):
            mts_val = solrMts[0].text
            dispatch_value(plugin_instance, mts_name, mts_val, 'counter')


def dispatch_core_timer_metrics(plugin_instance, cores_map, solr_metrics, default_dimensions):
    """Extract required timer metrics and dispatch to collectd"""
    corenum = None if 'error' in cores_map.keys() else 0
    for core in solr_metrics['metrics'].keys() if 'error' in cores_map.keys() else solr_metrics['metrics'][::2]:
        corenum = core if 'error' in cores_map.keys() else corenum + 1
        core = re.sub(r'solr\.core\.', '', core)
        core = re.sub(r'\.', '_', core)
        dimensions = prepare_dimensions(default_dimensions, core, cores_map)
        for mts_name in solr_metrics['metrics'][corenum].keys():
            amts_name = parse_mtsname(mts_name)
            if amts_name in CORE_GAUGE_METRICS:
                for reqTimes in solr_metrics['metrics'][corenum][mts_name].keys():
                    dmts_name = amts_name + '.' + reqTimes
                    mts_val = solr_metrics['metrics'][corenum][mts_name][reqTimes]
                    dispatch_value(plugin_instance, dmts_name, mts_val, 'gauge', dimensions)
        corenum = core if 'error' in cores_map.keys() else corenum + 1


def dispatch_timer_metrics(plugin_instance, solr_metrics, cores_map):
    """Extract required counter metrics and dispatch to collectd"""
    corenum = plugin_instance if 'error' in cores_map.keys() else 1
    for mts_name in solr_metrics['metrics'][corenum].keys():
        amts_name = parse_mtsname(mts_name)
        if any(amts_name in l for l in (NODE_GAUGE_METRICS, JVM_GAUGE_METRICS, JETTY_GAUGE_METRICS)):
            for reqTimes in solr_metrics['metrics'][corenum][mts_name].keys():
                dmts_name = amts_name + '.' + reqTimes
                mts_val = solr_metrics['metrics'][corenum][mts_name][reqTimes]
                dispatch_value(plugin_instance, dmts_name, mts_val, 'gauge')


def dispatch_core_gauge_metrics(plugin_instance, cores_map, solr_metrics, default_dimensions):
    """Extract required gauge metrics and dispatch to collectd"""
    dimensions = {}
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if mts_name == 'CORE.coreName':
            core = solrMts[0].text
            dimensions = prepare_dimensions(default_dimensions, core, cores_map)

        if mts_name in CORE_GAUGE_METRICS:
            mts_val = solrMts[0].text
            dispatch_value(plugin_instance, mts_name, mts_val, 'gauge', dimensions)


def dispatch_gauge_metrics(plugin_instance, solr_metrics, cores_map):
    """Extract required gauge metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if any(mts_name in l for l in (NODE_GAUGE_METRICS, JVM_GAUGE_METRICS, JETTY_GAUGE_METRICS)):
            mts_val = solrMts[0].text
            dispatch_value(plugin_instance, mts_name, mts_val, 'gauge')


def get_cores(data):
    url = '%s/solr/admin/cores?action=status' % data['base_url']
    cores = []
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        xml = etree.fromstring(f.read())
        cores = [lst.attrib['name'].strip() for lst in xml.findall('./lst/lst')]
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info, HTTP error: ' + str(e.code))
        log_verbose(url)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin get_cores: can\'t get info: ' + str(e.reason))
        log_verbose(url)

    return cores


def fetch_solr_stats(data, measure, registry):
    """Connect to Solr stat page and and return XML object"""
    url = '%s/solr/admin/metrics?wt=xml&type=%s&group=%s' % (data['base_url'], measure, registry)
    xml = None
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        xml = etree.fromstring(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ' + e.code)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)
    return xml


def fetch_solr_json_stats(data, measure, registry):
    """Connect to Solr stat page and and return JSON object"""
    url = '%s/solr/admin/metrics?wt=json&type=%s&group=%s' % (data['base_url'], measure, registry)
    log_verbose("Fetching %s" % url)
    f = urllib2.urlopen(url)
    json_data = json.loads(f.read())

    return json_data


def fetch_cores_info(data, core):
    """Connect to Solr stat page and and return XML object"""
    url = '%s/solr/admin/cores?action=status&core=%s' % (data['base_url'], core)
    xml = None
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        xml = etree.fromstring(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ' + e.code)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)
    return xml


def fetch_collections_info(data):
    """Connect to SolrCloud status page and and return JSON object"""
    url = '%s/solr/admin/collections?action=CLUSTERSTATUS&wt=json' % data['base_url']
    get_data = None
    cores_map = {}
    try:
        log_verbose("Fetching %s" % url)
        f = urllib2.urlopen(url)
        get_data = json.loads(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ')
        cores_map['error'] = 'Solr instance is not running in SolrCloud mode'
        return cores_map
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)

    if 'error' in get_data.keys():
        log_verbose('%s' % get_data['error']['msg'])
        cores_map['error'] = get_data['error']['msg']
    elif 'cluster' in get_data.keys():
        log_verbose('Solr running in SolrCloud mode')
        solrCollections = get_data['cluster']['collections'].keys()
        for collection in solrCollections:
            solrShards = get_data['cluster']['collections'][collection]['shards']
            for shard in solrShards.keys():
                for coreNodes in solrShards[shard]['replicas'].keys():
                    core = solrShards[shard]['replicas'][coreNodes]['core']
                    node = solrShards[shard]['replicas'][coreNodes]['node_name']
                    cores_map[core] = {'collection': collection, 'node': node, 'shard': shard}
    return cores_map


def prepare_dimensions(default_dimensions, core, cores_map):
    dimensions = {}
    if default_dimensions['cluster'] is False:
        dimensions['core'] = core
        dimensions['cluster'] = 'False'
    else:
        dimensions['collection'] = cores_map[core]['collection']
        dimensions['node'] = cores_map[core]['node']
        dimensions['shard'] = cores_map[core]['shard']
        dimensions['core'] = core
        dimensions['cluster'] = 'True'
    return dimensions


def read_callback(data):
    log_verbose('solr plugin: Read callback called')
    metric_registries = ['core', 'node', 'jvm', 'jetty']
    # measure_values = ['counter', 'gauge', 'meter', 'timer']
    measure_values = ['gauge', 'counter', 'timer', 'meter']
    cores_map = fetch_collections_info(data)
    cores = get_cores(data)

    log_verbose('solr plugin: Cores: ' + ' '.join(cores))

    default_dimensions = {'cluster': False if 'error' in cores_map.keys() else True, 'collection': None, 'shard': None,
                          'node': None, 'core': None}

    for core in cores:
        core_info = fetch_cores_info(data, core)
        if not core_info:
            collectd.error('solr plugin: No info received')

        # parse cores info
        plugin_instance = 'solr.core'
        for solrMts in core_info.findall('./lst/lst/lst/int'):
            mts_name = solrMts.attrib['name'].strip()
            if mts_name in CORE_SELF_METRICS:
                mts_val = solrMts.text
                # log_verbose('Solr metric: %s, Value : %s' % (mts_name, mts_val))
                dimensions = prepare_dimensions(default_dimensions, core, cores_map)
                dispatch_value(plugin_instance, mts_name, mts_val, 'gauge', dimensions)

    for registry in metric_registries:
        plugin_instance = 'solr.%s' % registry
        for measure in measure_values:
            # gauge and counter metrics should be updated to JSON
            if measure in ('gauge', 'counter'):
                solr_metrics = fetch_solr_stats(data, measure, registry)
            else:
                solr_metrics = fetch_solr_json_stats(data, measure, registry)
            if not solr_metrics:
                collectd.error('solr plugin: No info received')
                continue
            if registry == 'core':
                SOLR_CORE_METRIC_FUNC[measure](plugin_instance, cores_map, solr_metrics, default_dimensions)
            else:
                SOLR_METRIC_FUNC[measure](plugin_instance, solr_metrics, cores_map)


SOLR_METRIC_FUNC = {'counter': dispatch_counter_metrics,
                    'gauge': dispatch_gauge_metrics,
                    'meter': dispatch_timer_metrics,
                    'timer': dispatch_timer_metrics,
                    }
SOLR_CORE_METRIC_FUNC = {'counter': dispatch_core_counter_metrics,
                         'gauge': dispatch_core_gauge_metrics,
                         'meter': dispatch_core_timer_metrics,
                         'timer': dispatch_core_timer_metrics,
                         }
# register callbacks
collectd.register_config(configure_callback)
