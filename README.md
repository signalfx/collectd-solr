# collectd Apache Solr Plugin

An apache solr [collectd](http://www.collectd.org/) plugin which users can use to send metrics from solr instances to SignalFx

## Installation

* Checkout this repository somewhere on your system accessible by collectd. The suggested location is `/usr/share/collectd/`
* Configure the plugin (see below)
* Restart collectd

## Requirements

* collectd 4.9 or later (for the Python plugin)
* Python 2.6 or later
* solr 6.6 or later

## Configuration
The following are required configuration keys:

* Host - Required. Hostname or IP address of the solr node, default is 'localhost'
* Port - Required. The port of the solr node, default is '8983'

Optional configurations keys include:

* Interval - Interval between metric calls. Default is 10s
* Cluster - The cluster to which the node belongs. By default, this is set to "default"
* EnhancedMetrics - Flag to specify whether advanced stats from the `/metrics` endpoint are needed. Default is False
* IncludeMetric - Metrics from the `/metrics` endpoint can be included individually
* ExcludeMetric - Metrics from the `/metrics` endpoint can be excluded individually
* Dimension - Add extra dimensions to your metrics

Specify path to keyfile and certificate if certificate based authentication of clients is enabled on your solr node
* ssl_keyfile - path to file
* ssl_certificate - path to file

Provide a custom file that lists trusted CA certificates, required when keyfile and certificate are provided
* ssl_ca_certs - path to file

Note that multiple solr nodes can be configured in the same file.

```
LoadPlugin python
<Plugin python>
  ModulePath "/usr/share/collectd/collectd-solr"

  Import solr_collectd
  <Module solr_collectd>
    Host "localhost"
    Port "8983"
    Cluster "prod"
    Interval 10
    EnhancedMetrics False
    IncludeMetric "metrics.solr.jvm.buffers.mapped.MemoryUsed"
  </Module>
  <Module solr_collectd>
    Host "localhost"
    Port "7574"
    Cluster "prod"
    Interval 10
    EnhancedMetrics True
    ExcludeMetric "metrics.solr.jvm.gc.ParNew.time"
    Dimension foo bar
  </Module>
</Plugin>
```
