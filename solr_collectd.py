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

SOLR_METRICS_FILE = 'solr_metrics_list.txt'
LEADER = "Leader"
FOLLOWER = "Follower"
DEFAULT_INTERVAL = 10
DEFAULT_API_TIMEOUT = 60
PLUGIN_NAME = "solr"
VERBOSE_LOGGING = True
metrics_list = []


def log_verbose(msg):
    if not VERBOSE_LOGGING:
        return
    collectd.info('solr_info plugin [verbose]: %s' % msg)


def configure_callback(conf):
    """Receive configuration block"""
    global SOLR_METRICS_FILE
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
        elif val.key == 'SolrMetrics' and val.values[0]:
            SOLR_METRICS_FILE = val.values[0]

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


def load_metrics_list():
    global metrics_list
    # Open the file for reading.
    with open(SOLR_METRICS_FILE, 'r') as infile:
        raw_data = infile.read()  # Read the contents of the file into memory.
    # Return a list of the lines, breaking at line boundaries.
    metrics_list = raw_data.splitlines()


def parse_mtsname(mts_name):
    """Remove any slash (/) chars and duplicate attribute names"""
    mts_name = re.sub(r'(\.http://)', '.', mts_name)
    mts_name = re.sub(r'(\./|/)', '.', mts_name)
    mts_name = re.sub(r'ADMIN\.admin\.', 'ADMIN.', mts_name)
    mts_name = re.sub(r'QUERY\.query\.', 'QUERY.', mts_name)
    mts_name = re.sub(r'UPDATE\.update\.', 'UPDATE.', mts_name)
    mts_name = re.sub(r'REPLICATION\.replication\.', 'REPLICATION.', mts_name)
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
    # Uncomment below to send data over collectd-python plugin
    log_verbose('Emitting value: %s' % val)
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
            if mts_name in metrics_list:
                mts_val = solrMts[0].text
                dispatch_value(plugin_instance, mts_name, mts_val, 'counter', dimensions)


def dispatch_counter_metrics(plugin_instance, solr_metrics):
    """Extract required counter metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        mts_name = parse_mtsname(mts_name)
        if mts_name in metrics_list:
            mts_val = solrMts[0].text
            # log_verbose('Core: %s | Solr metric: %s, Value : %s' % (registry, mts_name, mts_val))
            dispatch_value(plugin_instance, mts_name, mts_val, 'counter')


def dispatch_core_timer_metrics(plugin_instance, cores_map, solr_metrics, default_dimensions):
    """Extract required timer metrics and dispatch to collectd"""
    corenum = 0
    for core in solr_metrics['metrics'][::2]:
        core = re.sub(r'solr\.core\.', '', core)
        core = re.sub(r'\.', '_', core)
        dimensions = prepare_dimensions(default_dimensions, core, cores_map)
        corenum += 1
        for mts_name in solr_metrics['metrics'][corenum].keys():
            amts_name = parse_mtsname(mts_name)
            if amts_name in metrics_list:
                for reqTimes in solr_metrics['metrics'][corenum][mts_name].keys():
                    dmts_name = amts_name + '.' + reqTimes
                    mts_val = solr_metrics['metrics'][corenum][mts_name][reqTimes]
                    dispatch_value(plugin_instance, dmts_name, mts_val, 'counter', dimensions)
        corenum += 1


def dispatch_timer_metrics(plugin_instance, solr_metrics):
    """Extract required counter metrics and dispatch to collectd"""
    for mts_name in solr_metrics['metrics'][1].keys():
        amts_name = parse_mtsname(mts_name)
        if amts_name in metrics_list:
            for reqTimes in solr_metrics['metrics'][1][mts_name].keys():
                dmts_name = amts_name + '.' + reqTimes
                mts_val = solr_metrics['metrics'][1][mts_name][reqTimes]
                dispatch_value(plugin_instance, dmts_name, mts_val, 'counter')


def dispatch_core_gauge_metrics(plugin_instance, cores_map, solr_metrics, default_dimensions):
    """Extract required gauge metrics and dispatch to collectd"""
    dimensions = {}
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if mts_name == 'CORE.coreName':
            core = solrMts[0].text
            dimensions = prepare_dimensions(default_dimensions, core, cores_map)

        if mts_name in metrics_list:
            mts_val = solrMts[0].text
            # for solrMtsVal in solrMts.findall('./'):
            #     mts_val = solrMtsVal[0].text
            # log_verbose('Core: %s | Solr metric: %s, Value : %s' % (core, mts_name, mts_val))
            dispatch_value(plugin_instance, mts_name, mts_val, 'gauge', dimensions)


def dispatch_gauge_metrics(plugin_instance, solr_metrics):
    """Extract required gauge metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if mts_name in metrics_list:
            mts_val = solrMts[0].text
            # log_verbose('Core: %s | Solr metric: %s, Value : %s' % (registry, mts_name, mts_val))
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
    f = urllib2.urlopen(url)
    json_data = json.loads(f.read())

    return json_data


def fetch_cores_info(data, core):
    """Connect to Solr stat page and and return XML object"""
    url = '%s/solr/admin/cores?action=status&core=%s' % (data['base_url'], core)
    xml = None
    try:
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
    f = urllib2.urlopen(url)
    get_data = json.loads(f.read())
    cores_map = {}

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
        dimensions['cluster'] = False
    else:
        dimensions['collection'] = cores_map[core]['collection']
        dimensions['node'] = cores_map[core]['node']
        dimensions['shard'] = cores_map[core]['shard']
        dimensions['core'] = core
    return dimensions


def read_callback(data):
    log_verbose('solr plugin: Read callback called')
    metric_registries = ['core', 'node', 'jvm', 'jetty']
    # measure_values = ['counter', 'gauge', 'meter', 'timer']
    measure_values = ['gauge', 'counter', 'timer', 'meter']
    load_metrics_list()
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
            if mts_name in metrics_list:
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
                SOLR_METRIC_FUNC[measure](plugin_instance, solr_metrics)


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
# collectd.register_read(read_callback)
