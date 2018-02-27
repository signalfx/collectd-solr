#!/usr/bin/env python
import collections
import mock
import sys
import pytest
import sample_responses


class MockCollectd(mock.MagicMock):

    @staticmethod
    def log(log_str):
        print log_str

    debug = log
    info = log
    warning = log
    error = log

sys.modules['collectd'] = MockCollectd()

import solr_collectd


def mock_api_call(url, opener=None):
    if '=CLUSTERSTATUS' in url:
        return sample_responses.collections

    if '/cores' in url:
        return sample_responses.cores

    if '/metrics' in url:
        return sample_responses.metrics

    if '=OVERSEERSTATUS' in url:
        return sample_responses.overseer

    if 'shards.info=' in url:
        return sample_responses.shards_info


ConfigOption = collections.namedtuple('ConfigOption', ('key', 'values'))

fail_mock_config_required_params = mock.Mock()
fail_mock_config_required_params.children = [
    ConfigOption('Host', ('localhost',)),
    ConfigOption('Testing', ('True'))
]


def test_config_fail():
    with pytest.raises(KeyError):
        solr_collectd.configure_callback(fail_mock_config_required_params)

mock_config = mock.Mock()
mock_config.children = [
    ConfigOption('Host', ('localhost', )),
    ConfigOption('Port', ('8983', )),
    ConfigOption('Cluster', ('MockSolrCluster', )),
    ConfigOption('Username', ('username', )),
    ConfigOption('Password', ('password', )),
    ConfigOption('Testing', ('True', )),
    ConfigOption('EnhancedMetrics', ('True', )),
    ConfigOption('IncludeMetric', ('metrics.solr.jvm.buffers.mapped.MemoryUsed', )),
    ConfigOption('ExcludeMetric', ('metrics.solr.jvm.gc.ParNew.time', ))
]


def test_default_config():
    module_config = solr_collectd.configure_callback(mock_config)
    assert module_config['plugin_conf']['Host'] == 'localhost'
    assert module_config['plugin_conf']['Port'] == '8983'
    assert module_config['username'] == 'username'
    assert module_config['password'] == 'password'
    assert module_config['base_url'] == "http://localhost:8983/solr"
    optional_metrics = module_config['include_optional_metrics']
    exclude_metrics = module_config['exclude_optional_metrics']
    assert optional_metrics is not None
    assert exclude_metrics is not None
    assert 'metrics.solr.jvm.buffers.mapped.MemoryUsed' in optional_metrics
    assert 'metrics.solr.jvm.gc.ParNew.time' in exclude_metrics


mock_config_ssl = mock.Mock()
mock_config_ssl.children = [
    ConfigOption('Host', ('localhost', )),
    ConfigOption('Port', ('8983', )),
    ConfigOption('Cluster', ('MockSolrCluster', )),
    ConfigOption('Username', ('username', )),
    ConfigOption('Password', ('password', )),
    ConfigOption('ssl_keyfile', ('ssl_keyfile', )),
    ConfigOption('ssl_certificate', ('ssl_certificate', )),
    ConfigOption('ssl_ca_certs', ('ssl_ca_certs', )),
    ConfigOption('Testing', ('True', ))
]


def test_config_ssl():
    module_config = solr_collectd.configure_callback(mock_config_ssl)
    assert module_config['plugin_conf']['Host'] == 'localhost'
    assert module_config['plugin_conf']['Port'] == '8983'
    assert module_config['username'] == 'username'
    assert module_config['password'] == 'password'
    assert module_config['base_url'] == "https://localhost:8983/solr"
    assert module_config['ssl_keys']['ssl_keyfile'] == 'ssl_keyfile'
    assert module_config['ssl_keys']['ssl_certificate'] == 'ssl_certificate'
    assert module_config['ssl_keys']['ssl_ca_certs'] == 'ssl_ca_certs'


@mock.patch('solr_collectd._api_call', mock_api_call)
def test_with_default_metrics():
    solr_collectd.read_metrics(solr_collectd.configure_callback(mock_config))
