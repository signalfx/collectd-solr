#! /usr/bin/python
#
# Collectd plugin for apache-solr
#

import collectd
import sys
import urllib2
import re

try:
    import xml.etree.cElementTree as etree
except ImportError:
    try:
        import xml.etree.ElementTree as etree
    except ImportError:
        print 'python >= 2.5'
        sys.exit()

# Host to connect to. Override in config by specifying 'Host'.
SOLR_HOST = 'localhost'
# Port to connect on. Override in config by specifying 'Port'.
SOLR_PORT = 8983
# Solr URL. Override in config by specifying 'SolrURL'.
SOLR_URL = 'solr'
# Solr Admin URL. Override in config by specifying 'SolrAdminURL'.
SOLR_ADMIN = 'admin'
# Solr Metrics API URL
SOLR_METRICS_URL = 'http://%s:%s/%s/%s' % (SOLR_HOST, SOLR_PORT, SOLR_URL, SOLR_ADMIN)
# SOLR_METRICS_URL = 'http://%s:%s/%s/admin/metrics?wt=xml&type=%s&group=%s'
SOLR_METRICS_FILE = 'solr_metrics_list.txt'

VERBOSE_LOGGING = True
metrics_list = []


def log_verbose(msg):
    if not VERBOSE_LOGGING:
        return
    collectd.info('solr_info plugin [verbose]: %s' % msg)


def configure_callback(conf):
    """Receive configuration block"""
    global SOLR_HOST, SOLR_PORT, SOLR_URL, SOLR_METRICS_FILE
    log_verbose("Configuring solr plugin with params: %s" % str(conf.children))
    for node in conf.children:
        if node.key == 'Host':
            SOLR_HOST = node.values[0]
        elif node.key == 'Port':
            SOLR_PORT = int(node.values[0])
        if node.key == 'URL':
            SOLR_URL = node.values[0]
        if node.key == 'SolrMetrics':
            SOLR_METRICS_FILE = node.values[0]
        else:
            collectd.warning('solr_collectd plugin: Unknown config key: %s.' % node.key)
    log_verbose('Configured: host=%s, port=%s, url=%s' % (SOLR_HOST, SOLR_PORT, SOLR_URL))


def load_metrics_list():
    global metrics_list
    # Open the file for reading.
    with open(SOLR_METRICS_FILE, 'r') as infile:
        raw_data = infile.read()  # Read the contents of the file into memory.
    # Return a list of the lines, breaking at line boundaries.
    metrics_list = raw_data.splitlines()


def parse_mtsname(mts_name):
    """Remove any slash (/) chars and duplicate attribute names"""
    mts_name = re.sub(r'(\./|/)', '.', mts_name)
    mts_name = re.sub(r'ADMIN\.admin\.', 'ADMIN.', mts_name)
    mts_name = re.sub(r'QUERY\.query\.', 'QUERY.', mts_name)
    mts_name = re.sub(r'UPDATE\.update\.', 'UPDATE.', mts_name)
    mts_name = re.sub(r'REPLICATION\.replication\.', 'REPLICATION.', mts_name)
    return mts_name


def get_cores():
    url = 'http://%s:%s/%s/admin/cores?action=status' % (SOLR_HOST, SOLR_PORT, SOLR_URL)
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


def dispatch_value(instance, key, value, value_type):
    """Dispatch a value to collectd"""
    log_verbose('Sending value: %s.%s=%s' % (instance, key, value))
    val = collectd.Values(plugin='solr')
    val.plugin_instance = instance
    val.type = value_type
    val.type_instance = key
    val.values = [value]
    # Uncomment below to send data over collectd-python plugin
    val.dispatch()


def dispatch_core_counter_metrics(cores, solr_metrics):
    """Extract required gauge metrics and dispatch to collectd"""
    core = cores[0]
    mts_val = ''
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        mts_name = parse_mtsname(mts_name)
        if mts_name in metrics_list:
            for solrMtsVal in solrMts.findall('./'):
                mts_val = solrMtsVal[0].text
            if mts_val in cores:
                core = mts_val
                continue
            log_verbose('Core: %s | Solr metric: %s, Value : %s' % (core, mts_name, mts_val))
            dispatch_value(core, mts_name, mts_val, 'counter')


def dispatch_counter_metrics(registry, solr_metrics):
    """Extract required counter metrics and dispatch to collectd"""
    mts_val = ''
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        mts_name = parse_mtsname(mts_name)
        if mts_name in metrics_list:
            for solrMtsVal in solrMts.findall('./'):
                mts_val = solrMtsVal[0].text
            log_verbose('Core: %s | Solr metric: %s, Value : %s' % (registry, mts_name, mts_val))
            dispatch_value(registry, mts_name, mts_val, 'counter')


# TODO
def dispatch_meter_metrics(core, solr_metrics):
    """Extract required counter metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst/int'):
        mts_name = solrMts.attrib['name'].strip()
        mts_val = solrMts.text
        log_verbose('Solr metric: %s, Value : %s' % (mts_name, mts_val))
        dispatch_value(core, mts_name, mts_val, 'counter')


# TODO
def dispatch_timer_metrics(core, solr_metrics):
    """Extract required counter metrics and dispatch to collectd"""
    for solrMts in solr_metrics.findall('./lst/lst/lst/int'):
        mts_name = solrMts.attrib['name'].strip()
        mts_val = solrMts.text
        log_verbose('Solr metric: %s, Value : %s' % (mts_name, mts_val))
        dispatch_value(core, mts_name, mts_val, 'counter')


def dispatch_core_gauge_metrics(cores, solr_metrics):
    """Extract required gauge metrics and dispatch to collectd"""
    core = cores[0]
    mts_val = ''
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if mts_name in metrics_list:
            for solrMtsVal in solrMts.findall('./'):
                mts_val = solrMtsVal[0].text
            if mts_val in cores:
                core = mts_val
                continue
            log_verbose('Core: %s | Solr metric: %s, Value : %s' % (core, mts_name, mts_val))
            dispatch_value(core, mts_name, mts_val, 'gauge')


def dispatch_gauge_metrics(registry, solr_metrics):
    """Extract required gauge metrics and dispatch to collectd"""
    mts_val = ''
    for solrMts in solr_metrics.findall('./lst/lst/lst'):
        mts_name = solrMts.attrib['name'].strip()
        if mts_name in metrics_list:
            for solrMtsVal in solrMts.findall('./'):
                mts_val = solrMtsVal[0].text
            log_verbose('Core: %s | Solr metric: %s, Value : %s' % (registry, mts_name, mts_val))
            dispatch_value(registry, mts_name, mts_val, 'gauge')


def fetch_solr_stats(measure, registry):
    """Connect to Solr stat page and and return XML object"""
    # Uncomment below when required to get complete stats
    # url = 'http://%s:%s/%s/%s/%s' % (SOLR_HOST, SOLR_PORT, SOLR_URL, core, SOLR_ADMIN_URL)
    url = SOLR_METRICS_URL + '/metrics?wt=xml&type=%s&group=%s' % (measure, registry)
    xml = None
    try:
        f = urllib2.urlopen(url)
        # f = open('queues.xml', 'r')
        xml = etree.fromstring(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ' + e.code)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)
    return xml


def fetch_cores_info(core):
    """Connect to Solr stat page and and return XML object"""
    url = 'http://%s:%s/%s/admin/cores?action=status&core=%s' % (SOLR_HOST, SOLR_PORT, SOLR_URL, core)
    xml = None
    try:
        f = urllib2.urlopen(url)
        xml = etree.fromstring(f.read())
    except urllib2.HTTPError as e:
        log_verbose('solr_collectd plugin: can\'t get info, HTTP error: ' + e.code)
    except urllib2.URLError as e:
        log_verbose('solr_collectd plugin: can\'t get info: ' + e.reason)
    return xml


def read_callback():
    log_verbose('solr plugin: Read callback called')
    metric_registries = ['core', 'node', 'jvm', 'jetty']
    # measure_values = ['counter', 'gauge', 'meter', 'timer']
    measure_values = ['gauge', 'counter']
    load_metrics_list()
    cores = get_cores()
    log_verbose('solr plugin: Cores: ' + ' '.join(cores))

    for core in cores:
        core_info = fetch_cores_info(core)
        if not core_info:
            collectd.error('solr plugin: No info received')

        # parse cores info
        for solrMts in core_info.findall('./lst/lst/lst/int'):
            mts_name = solrMts.attrib['name'].strip()
            if mts_name in metrics_list:
                mts_val = solrMts.text
                log_verbose('Solr metric: %s, Value : %s' % (mts_name, mts_val))
                dispatch_value(core, mts_name, mts_val, 'gauge')

    for registry in metric_registries:
        for measure in measure_values:
            solr_metrics = fetch_solr_stats(measure, registry)
            if not solr_metrics:
                collectd.error('solr plugin: No info received')
                continue
            if registry == 'core':
                SOLR_CORE_METRIC_FUNC[measure](cores, solr_metrics)
            else:
                SOLR_METRIC_FUNC[measure](registry, solr_metrics)


SOLR_METRIC_FUNC = {'counter': dispatch_counter_metrics,
                    'gauge': dispatch_gauge_metrics,
                    'meter': dispatch_meter_metrics,
                    'timer': dispatch_timer_metrics,
                    }
SOLR_CORE_METRIC_FUNC = {'counter': dispatch_core_counter_metrics,
                         'gauge': dispatch_core_gauge_metrics,
                         'meter': dispatch_meter_metrics,
                         'timer': dispatch_timer_metrics,
                         }
# register callbacks
collectd.register_config(configure_callback)
collectd.register_read(read_callback)
