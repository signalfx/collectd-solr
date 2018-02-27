collections = {
    "responseHeader": {
        "status": 0,
        "QTime": 0
    },
    "cluster": {
        "collections": {
            "demo_collection": {
                "replicationFactor": "1",
                "shards": {
                    "shard1": {
                        "range": "80000000-7fffffff",
                        "state": "active",
                        "replicas": {
                            "core_node1": {
                                "core": "demo_collection_shard1_replica1",
                                "base_url": "http://172.31.45.252:7575/solr",
                                "node_name": "172.31.45.252:7575_solr",
                                "state": "active",
                                "leader": "true"
                            }
                        }
                    }
                },
                "router": {
                    "name": "compositeId"
                },
                "maxShardsPerNode": "1",
                "autoAddReplicas": "false",
                "znodeVersion": 3,
                "configName": "demo_collection"
            },
            "cfxlabs": {
                "replicationFactor": "2",
                "shards": {
                    "shard1": {
                        "range": "80000000-ffffffff",
                        "state": "active",
                        "replicas": {
                            "core_node1": {
                                "core": "cfxlabs_shard1_replica2",
                                "base_url": "http://172.31.45.252:8983/solr",
                                "node_name": "172.31.45.252:8983_solr",
                                "state": "active"
                            },
                            "core_node4": {
                                "core": "cfxlabs_shard1_replica1",
                                "base_url": "http://172.31.45.252:7575/solr",
                                "node_name": "172.31.45.252:7575_solr",
                                "state": "active",
                                "leader": "true"
                            }
                        }
                    },
                    "shard2": {
                        "range": "0-7fffffff",
                        "state": "active",
                        "replicas": {
                            "core_node2": {
                                "core": "cfxlabs_shard2_replica1",
                                "base_url": "http://172.31.45.252:8984/solr",
                                "node_name": "172.31.45.252:8984_solr",
                                "state": "active",
                                "leader": "true"
                            },
                            "core_node3": {
                                "core": "cfxlabs_shard2_replica2",
                                "base_url": "http://172.31.45.252:7574/solr",
                                "node_name": "172.31.45.252:7574_solr",
                                "state": "active"
                            }
                        }
                    }
                },
                "router": {
                    "name": "compositeId"
                },
                "maxShardsPerNode": "1",
                "autoAddReplicas": "false",
                "znodeVersion": 6,
                "configName": "cfxlabs"
            }
        },
        "live_nodes": [
            "172.31.45.252:7574_solr",
            "172.31.45.252:8984_solr",
            "172.31.45.252:7575_solr",
            "172.31.45.252:8983_solr"
        ]
    }
}

overseer = {
    "responseHeader": {
        "status": 0,
        "QTime": 10
    },
    "leader": "172.31.34.16:8983_solr",
    "overseer_queue_size": 0,
    "overseer_work_queue_size": 0,
    "overseer_collection_queue_size": 2,
    "overseer_operations": [
        "leader",
        {
            "requests": 61,
            "errors": 0,
            "avgRequestsPerSecond": 0.00012761992036317075,
            "5minRateRequestsPerSecond": 1.4821969375e-313,
            "15minRateRequestsPerSecond": 2.7550721534436908e-210,
            "avgTimePerRequest": 0.056257790750365314,
            "medianRequestTime": 0.065204,
            "75thPcRequestTime": 0.066877,
            "95thPcRequestTime": 0.077564,
            "99thPcRequestTime": 0.077564,
            "999thPcRequestTime": 0.091823
        }
    ]
}

shards_info = {
  "responseHeader": {
    "zkConnected": "true",
    "status": 0,
    "QTime": 5,
    "params": {
      "q": "*:*",
      "shards.info": "true",
      "wt": "json"
    }
  },
  "shards.info": {
    "http://172.31.45.252:7574/solr/cfxlabs_shard2_replica1/|http://172.31.45.252:7575/solr/cfxlabs_shard2_replica2/": {
      "numFound": 21,
      "maxScore": 1,
      "shardAddress": "http://172.31.45.252:7574/solr/cfxlabs_shard2_replica1",
      "time": 2
    },
    "http://172.31.45.252:8984/solr/cfxlabs_shard1_replica1/|http://172.31.45.252:8983/solr/cfxlabs_shard1_replica2/": {
      "numFound": 15,
      "maxScore": 1,
      "shardAddress": "http://172.31.45.252:8984/solr/cfxlabs_shard1_replica1",
      "time": 2
    }
  },
  "response": {
    "numFound": 36,
    "start": 0,
    "maxScore": 1,
    "docs": [
      {
        "id": "SP2514N",
        "name": [
          "Samsung SpinPoint P120 SP2514N - hard drive - 250 GB - ATA-133"
        ],
        "manu": [
          "Samsung Electronics Co. Ltd."
        ],
        "manu_id_s": "samsung",
        "cat": [
          "electronics",
          "hard drive"
        ],
        "features": [
          "7200RPM, 8MB cache, IDE Ultra ATA-133",
          "NoiseGuard, SilentSeek technology, Fluid Dynamic Bearing (FDB) motor"
        ],
        "price": [
          92
        ],
        "popularity": [
          6
        ],
        "inStock": [
          "true"
        ],
        "manufacturedate_dt": "2006-02-13T15:26:37Z",
        "store": [
          "35.0752,-97.032"
        ],
        "_version_": 1586194703158608000
      },
      {
        "id": "6H500F0",
        "name": [
          "Maxtor DiamondMax 11 - hard drive - 500 GB - SATA-300"
        ],
        "manu": [
          "Maxtor Corp."
        ],
        "manu_id_s": "maxtor",
        "cat": [
          "electronics",
          "hard drive"
        ],
        "features": [
          "SATA 3.0Gb/s, NCQ",
          "8.5ms seek",
          "16MB cache"
        ],
        "price": [
          350
        ],
        "popularity": [
          6
        ],
        "inStock": [
          "true"
        ],
        "store": [
          "45.17614,-93.87341"
        ],
        "manufacturedate_dt": "2006-02-13T15:26:37Z",
        "_version_": 1586194703571746800
      },
      {
        "id": "F8V7067-APL-KIT",
        "name": [
          "Belkin Mobile Power Cord for iPod w/ Dock"
        ],
        "manu": [
          "Belkin"
        ],
        "manu_id_s": "belkin",
        "cat": [
          "electronics",
          "connector"
        ],
        "features": [
          "car power adapter, white"
        ],
        "weight": [
          4
        ],
        "price": [
          19.95
        ],
        "popularity": [
          1
        ],
        "inStock": [
          "false"
        ],
        "store": [
          "45.18014,-93.87741"
        ],
        "manufacturedate_dt": "2005-08-01T16:30:25Z",
        "_version_": 1586194705123639300
      },
      {
        "id": "apple",
        "compName_s": "Apple",
        "address_s": "1 Infinite Way, Cupertino CA",
        "_version_": 1586194706938724400
      },
      {
        "id": "ati",
        "compName_s": "ATI Technologies",
        "address_s": "33 Commerce Valley Drive East Thornhill, ON L3T 7N6 Canada",
        "_version_": 1586194706942918700
      },
      {
        "id": "canon",
        "compName_s": "Canon, Inc.",
        "address_s": "One Canon Plaza Lake Success, NY 11042",
        "_version_": 1586194707013173200
      },
      {
        "id": "corsair",
        "compName_s": "Corsair Microsystems",
        "address_s": "46221 Landing Parkway Fremont, CA 94538",
        "_version_": 1586194707016319000
      },
      {
        "id": "dell",
        "compName_s": "Dell, Inc.",
        "address_s": "One Dell Way Round Rock, Texas 78682",
        "_version_": 1586194707017367600
      },
      {
        "id": "samsung",
        "compName_s": "Samsung Electronics Co. Ltd.",
        "address_s": "105 Challenger Rd. Ridgefield Park, NJ 07660-0511",
        "_version_": 1586194707019464700
      },
      {
        "id": "viewsonic",
        "compName_s": "ViewSonic Corp",
        "address_s": "381 Brea Canyon Road Walnut, CA 91789-0708",
        "_version_": 1586194707020513300
      }
    ]
  }
}

cores = {
    "responseHeader": {
        "status": 0,
        "QTime": 0
    },
    "initFailures": {},
    "status": {
        "cfxlabs_shard1_replica1": {
            "name": "cfxlabs_shard1_replica1",
            "instanceDir": "/opt/solr/example/cloud/node4/solr/cfxlabs_shard1_replica1",
            "dataDir": "/opt/solr/example/cloud/node4/solr/cfxlabs_shard1_replica1/data/",
            "config": "solrconfig.xml",
            "schema": "managed-schema",
            "startTime": "2017-11-28T06:27:10.029Z",
            "uptime": 1924790335,
            "lastPublished": "active",
            "configVersion": 0,
            "cloud": {
                "collection": "cfxlabs",
                "shard": "shard1",
                "replica": "core_node4"
            },
            "index": {
                "numDocs": 15,
                "maxDoc": 15,
                "deletedDocs": 0,
                "indexHeapUsageBytes": -1,
                "version": 14,
                "segmentCount": 4,
                "current": "true",
                "hasDeletions": "false",
                "directory": "org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@/opt/solr-6.6.2/example/cloud/node4/solr/cfxlabs_shard1_replica1/data/index lockFactory=org.apache.lucene.store.NativeFSLockFactory@63ac848d; maxCacheMB=48.0 maxMergeSizeMB=4.0)",
                "segmentsFile": "segments_3",
                "segmentsFileSizeInBytes": 351,
                "userData": {
                    "commitTimeMSec": "1512713858998"
                },
                "lastModified": "2017-12-08T06:17:38.998Z",
                "sizeInBytes": 35531,
                "size": "34.7 KB"
            }
        },
        "demo_collection_shard1_replica1": {
            "name": "demo_collection_shard1_replica1",
            "instanceDir": "/opt/solr/example/cloud/node4/solr/demo_collection_shard1_replica1",
            "dataDir": "/opt/solr/example/cloud/node4/solr/demo_collection_shard1_replica1/data/",
            "config": "solrconfig.xml",
            "schema": "managed-schema",
            "startTime": "2017-12-19T16:29:31.817Z",
            "uptime": 74248548,
            "lastPublished": "active",
            "configVersion": 0,
            "cloud": {
                "collection": "demo_collection",
                "shard": "shard1",
                "replica": "core_node1"
            },
            "index": {
                "numDocs": 10,
                "maxDoc": 10,
                "deletedDocs": 0,
                "indexHeapUsageBytes": -1,
                "version": 6,
                "segmentCount": 1,
                "current": "true",
                "hasDeletions": "false",
                "directory": "org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@/opt/solr-6.6.2/example/cloud/node4/solr/demo_collection_shard1_replica1/data/index lockFactory=org.apache.lucene.store.NativeFSLockFactory@63ac848d; maxCacheMB=48.0 maxMergeSizeMB=4.0)",
                "segmentsFile": "segments_2",
                "segmentsFileSizeInBytes": 165,
                "userData": {
                    "commitTimeMSec": "1512716643174"
                },
                "lastModified": "2017-12-08T07:04:03.174Z",
                "sizeInBytes": 7030,
                "size": "6.87 KB"
            }
        }
    }
}

metrics = {
    "responseHeader": {
        "status": 0,
        "QTime": 5
    },
    "metrics": {
        "solr.jetty": {
            "org.eclipse.jetty.server.handler.DefaultHandler.1xx-responses": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.2xx-responses": {
                "count": 162389,
                "meanRate": 0.08436070649762367,
                "1minRate": 0.33116069638241086,
                "5minRate": 0.30937877210458425,
                "15minRate": 0.30359368697558997
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.3xx-responses": {
                "count": 174,
                "meanRate": 0.00009039259389882247,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.9918150732115164e-133,
                "15minRate": 6.283566238819078e-46
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.4xx-responses": {
                "count": 15,
                "meanRate": 0.000007792464991302653,
                "1minRate": 2.964393875e-314,
                "5minRate": 4.443790618256286e-111,
                "15minRate": 1.2228731448048537e-39
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.5xx-responses": {
                "count": 27,
                "meanRate": 0.000014026436984400353,
                "1minRate": 2.964393875e-314,
                "5minRate": 8.398608680236134e-110,
                "15minRate": 1.2909519884114105e-38
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.active-dispatches": {
                "count": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.active-requests": {
                "count": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.active-suspended": {
                "count": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.async-dispatches": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.async-timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.connect-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.delete-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.dispatches": {
                "count": 162605,
                "meanRate": 0.0844729179617692,
                "1minRate": 0.33116069638241086,
                "5minRate": 0.30937877210458425,
                "15minRate": 0.30359368697558997,
                "min_ms": 0,
                "max_ms": 70,
                "mean_ms": 7.633202122060519,
                "median_ms": 1,
                "stddev_ms": 9.905076323973098,
                "p75_ms": 17,
                "p95_ms": 25,
                "p99_ms": 25,
                "p999_ms": 52
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.get-requests": {
                "count": 161430,
                "meanRate": 0.08386250822876681,
                "1minRate": 0.33116069638241086,
                "5minRate": 0.30937877210458425,
                "15minRate": 0.30359368697558997,
                "min_ms": 0,
                "max_ms": 70,
                "mean_ms": 7.6456825090761225,
                "median_ms": 1,
                "stddev_ms": 9.901228912285395,
                "p75_ms": 17,
                "p95_ms": 25,
                "p99_ms": 25,
                "p999_ms": 52
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.head-requests": {
                "count": 3,
                "meanRate": 0.0000015584929980018878,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 1,
                "max_ms": 6,
                "mean_ms": 1.0000000000000002,
                "median_ms": 1,
                "stddev_ms": 3.740326005275057e-10,
                "p75_ms": 1,
                "p95_ms": 1,
                "p99_ms": 1,
                "p999_ms": 1
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.move-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.options-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.other-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-4xx-15m": {
                "value": 4.027992666735449e-39
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-4xx-1m": {
                "value": 8.951526879e-314
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-4xx-5m": {
                "value": 1.4363592524551363e-110
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-5xx-15m": {
                "value": 4.2522359449299343e-38
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-5xx-1m": {
                "value": 8.951526879e-314
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.percent-5xx-5m": {
                "value": 2.7146686965959704e-109
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.post-requests": {
                "count": 1172,
                "meanRate": 0.0006088512645420488,
                "1minRate": 2.964393875e-314,
                "5minRate": 2.504489167813616e-97,
                "15minRate": 3.0594977785347026e-33,
                "min_ms": 0,
                "max_ms": 22,
                "mean_ms": 0.5109554226948172,
                "median_ms": 1,
                "stddev_ms": 0.499881508200168,
                "p75_ms": 1,
                "p95_ms": 1,
                "p99_ms": 1,
                "p999_ms": 1
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.put-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.requests": {
                "count": 162605,
                "meanRate": 0.08447291792753753,
                "1minRate": 0.33116069638241086,
                "5minRate": 0.30937877210458425,
                "15minRate": 0.30359368697558997,
                "min_ms": 0,
                "max_ms": 70,
                "mean_ms": 7.645682509076124,
                "median_ms": 1,
                "stddev_ms": 9.901228912285395,
                "p75_ms": 17,
                "p95_ms": 25,
                "p99_ms": 25,
                "p999_ms": 52
            },
            "org.eclipse.jetty.server.handler.DefaultHandler.trace-requests": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "org.eclipse.jetty.util.thread.QueuedThreadPool.qtp317983781.jobs": {
                "value": 1
            },
            "org.eclipse.jetty.util.thread.QueuedThreadPool.qtp317983781.size": {
                "value": 10
            },
            "org.eclipse.jetty.util.thread.QueuedThreadPool.qtp317983781.utilization": {
                "value": 0.2
            },
            "org.eclipse.jetty.util.thread.QueuedThreadPool.qtp317983781.utilization-max": {
                "value": 0.0002
            }
        },
        "solr.core.demo_collection.shard1.replica1": {
            "ADMIN./admin/file.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/file.requests": {
                "count": 0
            },
            "ADMIN./admin/file.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.totalTime": {
                "count": 0
            },
            "ADMIN./admin/logging.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/logging.requests": {
                "count": 0
            },
            "ADMIN./admin/logging.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.totalTime": {
                "count": 0
            },
            "ADMIN./admin/luke.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.requestTimes": {
                "count": 10,
                "meanRate": 0.000009442441607770824,
                "1minRate": 2.964393875e-314,
                "5minRate": 6.402380559290289e-109,
                "15minRate": 1.1278705796619868e-38,
                "min_ms": 0.089746,
                "max_ms": 1.822858,
                "mean_ms": 1.1412809641338695,
                "median_ms": 1.141281,
                "stddev_ms": 0.00021673691095245272,
                "p75_ms": 1.141281,
                "p95_ms": 1.141281,
                "p99_ms": 1.141281,
                "p999_ms": 1.141281
            },
            "ADMIN./admin/luke.requests": {
                "count": 10
            },
            "ADMIN./admin/luke.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.totalTime": {
                "count": 4062126
            },
            "ADMIN./admin/mbeans.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.requestTimes": {
                "count": 2,
                "meanRate": 0.0000018884883241858185,
                "1minRate": 2.964393875e-314,
                "5minRate": 2.9424078323584e-110,
                "15minRate": 3.6340108982235266e-39,
                "min_ms": 1.561797,
                "max_ms": 1.643746,
                "mean_ms": 1.576564125818505,
                "median_ms": 1.561797,
                "stddev_ms": 0.03149735209126498,
                "p75_ms": 1.561797,
                "p95_ms": 1.643746,
                "p99_ms": 1.643746,
                "p999_ms": 1.643746
            },
            "ADMIN./admin/mbeans.requests": {
                "count": 2
            },
            "ADMIN./admin/mbeans.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.totalTime": {
                "count": 3205543
            },
            "ADMIN./admin/ping.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.requestTimes": {
                "count": 9,
                "meanRate": 0.000008498197445491457,
                "1minRate": 2.964393875e-314,
                "5minRate": 3.3453120003611457e-110,
                "15minRate": 4.9815893853536946e-39,
                "min_ms": 0.055741,
                "max_ms": 0.088451,
                "mean_ms": 0.06668845071659316,
                "median_ms": 0.068568,
                "stddev_ms": 0.011811425717122296,
                "p75_ms": 0.068568,
                "p95_ms": 0.088451,
                "p99_ms": 0.088451,
                "p999_ms": 0.088451
            },
            "ADMIN./admin/ping.requests": {
                "count": 9
            },
            "ADMIN./admin/ping.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.totalTime": {
                "count": 579776
            },
            "ADMIN./admin/plugins.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/plugins.requests": {
                "count": 0
            },
            "ADMIN./admin/plugins.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.totalTime": {
                "count": 0
            },
            "ADMIN./admin/properties.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/properties.requests": {
                "count": 0
            },
            "ADMIN./admin/properties.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.totalTime": {
                "count": 0
            },
            "ADMIN./admin/segments.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.requestTimes": {
                "count": 1,
                "meanRate": 9.442441606690984e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.2282486939650232e-110,
                "15minRate": 1.7161644265062836e-39,
                "min_ms": 4.269951,
                "max_ms": 4.269951,
                "mean_ms": 4.269951,
                "median_ms": 4.269951,
                "stddev_ms": 0,
                "p75_ms": 4.269951,
                "p95_ms": 4.269951,
                "p99_ms": 4.269951,
                "p999_ms": 4.269951
            },
            "ADMIN./admin/segments.requests": {
                "count": 1
            },
            "ADMIN./admin/segments.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.totalTime": {
                "count": 4269951
            },
            "ADMIN./admin/system.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.requestTimes": {
                "count": 9,
                "meanRate": 0.000008498197457906736,
                "1minRate": 2.964393875e-314,
                "5minRate": 3.3453120003611457e-110,
                "15minRate": 4.9815893853536946e-39,
                "min_ms": 5.375108,
                "max_ms": 20.428003,
                "mean_ms": 13.093716235418562,
                "median_ms": 12.188356,
                "stddev_ms": 6.807672741711983,
                "p75_ms": 20.428003,
                "p95_ms": 20.428003,
                "p99_ms": 20.428003,
                "p999_ms": 20.428003
            },
            "ADMIN./admin/system.requests": {
                "count": 9
            },
            "ADMIN./admin/system.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.totalTime": {
                "count": 92537557
            },
            "ADMIN./admin/threads.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/threads.requests": {
                "count": 0
            },
            "ADMIN./admin/threads.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.totalTime": {
                "count": 0
            },
            "ADMIN./config.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./config.requests": {
                "count": 0
            },
            "ADMIN./config.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.totalTime": {
                "count": 0
            },
            "ADMIN./schema.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./schema.requests": {
                "count": 0
            },
            "ADMIN./schema.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.totalTime": {
                "count": 0
            },
            "CACHE.core.fieldCache": {
                "value": {
                    "entries_count": 0,
                    "total_size": "0 bytes"
                }
            },
            "CACHE.searcher.QUERY_DOC_FV": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.documentCache": {
                "value": {
                    "lookups": 14880,
                    "evictions": 0,
                    "cumulative_inserts": 10,
                    "cumulative_hits": 14870,
                    "hits": 14870,
                    "cumulative_evictions": 0,
                    "size": 10,
                    "hitratio": 1,
                    "cumulative_lookups": 14880,
                    "cumulative_hitratio": 1,
                    "warmupTime": 0,
                    "inserts": 10
                }
            },
            "CACHE.searcher.fieldValueCache": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.filterCache": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.perSegFilter": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.queryResultCache": {
                "value": {
                    "lookups": 1488,
                    "evictions": 0,
                    "cumulative_inserts": 1,
                    "cumulative_hits": 1487,
                    "hits": 1487,
                    "cumulative_evictions": 0,
                    "size": 1,
                    "hitratio": 1,
                    "cumulative_lookups": 1488,
                    "cumulative_hitratio": 1,
                    "warmupTime": 0,
                    "inserts": 1
                }
            },
            "CORE.aliases": {
                "value": [
                    "demo_collection_shard1_replica1"
                ]
            },
            "CORE.collection": {
                "value": "demo_collection"
            },
            "CORE.coreName": {
                "value": "demo_collection_shard1_replica1"
            },
            "CORE.fs.totalSpace": {
                "value": 8318783488
            },
            "CORE.fs.usableSpace": {
                "value": 5051539456
            },
            "CORE.indexDir": {
                "value": "/opt/solr/example/cloud/node4/solr/demo_collection_shard1_replica1/data/index/"
            },
            "CORE.instanceDir": {
                "value": "/opt/solr/example/cloud/node4/solr/demo_collection_shard1_replica1"
            },
            "CORE.refCount": {
                "value": 1
            },
            "CORE.shard": {
                "value": "shard1"
            },
            "CORE.startTime": {
                "value": "2017-12-19T16:29:31.817Z"
            },
            "INDEX.size": {
                "value": "6.87 KB"
            },
            "INDEX.sizeInBytes": {
                "value": 7030
            },
            "QUERY./browse.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./browse.requests": {
                "count": 0
            },
            "QUERY./browse.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.totalTime": {
                "count": 0
            },
            "QUERY./debug/dump.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./debug/dump.requests": {
                "count": 0
            },
            "QUERY./debug/dump.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.totalTime": {
                "count": 0
            },
            "QUERY./export.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./export.requests": {
                "count": 0
            },
            "QUERY./export.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.totalTime": {
                "count": 0
            },
            "QUERY./get.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./get.requests": {
                "count": 0
            },
            "QUERY./get.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.totalTime": {
                "count": 0
            },
            "QUERY./graph.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./graph.requests": {
                "count": 0
            },
            "QUERY./graph.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.totalTime": {
                "count": 0
            },
            "QUERY./query.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./query.requests": {
                "count": 0
            },
            "QUERY./query.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.totalTime": {
                "count": 0
            },
            "QUERY./select.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.requestTimes": {
                "count": 1492,
                "meanRate": 0.00140881229189031,
                "1minRate": 2.964393875e-314,
                "5minRate": 3.496977275359494e-97,
                "15minRate": 3.97274450288854e-33,
                "min_ms": 0.138387,
                "max_ms": 0.229617,
                "mean_ms": 0.1492321604444895,
                "median_ms": 0.146449,
                "stddev_ms": 0.006651530207211743,
                "p75_ms": 0.152028,
                "p95_ms": 0.162109,
                "p99_ms": 0.169695,
                "p999_ms": 0.187105
            },
            "QUERY./select.requests": {
                "count": 1492
            },
            "QUERY./select.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.totalTime": {
                "count": 284798347
            },
            "QUERY./sql.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./sql.requests": {
                "count": 0
            },
            "QUERY./sql.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.totalTime": {
                "count": 0
            },
            "QUERY./stream.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./stream.requests": {
                "count": 0
            },
            "QUERY./stream.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.totalTime": {
                "count": 0
            },
            "REPLICATION./replication.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.requestTimes": {
                "count": 9,
                "meanRate": 0.000008498197405646295,
                "1minRate": 2.964393875e-314,
                "5minRate": 3.3453120003611457e-110,
                "15minRate": 4.9815893853536946e-39,
                "min_ms": 0.188555,
                "max_ms": 3.492925,
                "mean_ms": 0.20758133562656736,
                "median_ms": 0.220932,
                "stddev_ms": 0.016607122613091496,
                "p75_ms": 0.220932,
                "p95_ms": 0.224305,
                "p99_ms": 0.224305,
                "p999_ms": 0.224305
            },
            "REPLICATION./replication.requests": {
                "count": 9
            },
            "REPLICATION./replication.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.totalTime": {
                "count": 10106797
            },
            "SEARCHER.new": {
                "count": 5
            },
            "SEARCHER.new.errors": {
                "count": 0
            },
            "SEARCHER.new.maxReached": {
                "count": 0
            },
            "SEARCHER.new.time": {
                "count": 5,
                "meanRate": 0.000004721220475459305,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.6466394421636964e-110,
                "15minRate": 3.003882634337879e-39,
                "min_ms": 1.540683,
                "max_ms": 7.821943,
                "mean_ms": 4.681313,
                "median_ms": 1.605002,
                "stddev_ms": 3.14063,
                "p75_ms": 7.821943,
                "p95_ms": 7.821943,
                "p99_ms": 7.821943,
                "p999_ms": 7.821943
            },
            "SEARCHER.new.warmup": {
                "count": 2,
                "meanRate": 0.0000018884881901893605,
                "1minRate": 2.964393875e-314,
                "5minRate": 8.233197210818482e-111,
                "15minRate": 1.5019413171689395e-39,
                "min_ms": 0.033153,
                "max_ms": 0.046435,
                "mean_ms": 0.033153,
                "median_ms": 0.033153,
                "stddev_ms": 0,
                "p75_ms": 0.033153,
                "p95_ms": 0.033153,
                "p99_ms": 0.033153,
                "p999_ms": 0.033153
            },
            "SEARCHER.searcher": {
                "value": {
                    "numDocs": 10,
                    "searcherName": "Searcher@59b89e32[demo_collection_shard1_replica1] main",
                    "reader": "ExitableDirectoryReader(UninvertingDirectoryReader(Uninverting(_0(6.6.2):C10)))",
                    "deletedDocs": 0,
                    "registeredAt": "2017-12-19T16:29:31.953Z",
                    "maxDoc": 10,
                    "indexVersion": 6,
                    "warmupTime": 0,
                    "caching": "true",
                    "readerDir": "org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@/opt/solr-6.6.2/example/cloud/node4/solr/demo_collection_shard1_replica1/data/index lockFactory=org.apache.lucene.store.NativeFSLockFactory@63ac848d; maxCacheMB=48.0 maxMergeSizeMB=4.0)",
                    "openedAt": "2017-12-19T16:29:31.952Z"
                }
            },
            "TLOG.applyingBuffered.ops": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "TLOG.buffered.ops": {
                "value": 0
            },
            "TLOG.replay.ops": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "TLOG.replay.remaining.bytes": {
                "value": 1422
            },
            "TLOG.replay.remaining.logs": {
                "value": 1
            },
            "TLOG.state": {
                "value": 3
            },
            "UPDATE./update.clientErrors": {
                "count": 1,
                "meanRate": 9.442441153518801e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE./update.errors": {
                "count": 1,
                "meanRate": 9.442441153462381e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE./update.requestTimes": {
                "count": 4,
                "meanRate": 0.000003776976461448238,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 2.553857,
                "max_ms": 81.194185,
                "mean_ms": 15.28413483173522,
                "median_ms": 2.628415,
                "stddev_ms": 25.970105544879868,
                "p75_ms": 2.628415,
                "p95_ms": 81.194185,
                "p99_ms": 81.194185,
                "p999_ms": 81.194185
            },
            "UPDATE./update.requests": {
                "count": 4
            },
            "UPDATE./update.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.totalTime": {
                "count": 130781028
            },
            "UPDATE./update/csv.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/csv.requests": {
                "count": 0
            },
            "UPDATE./update/csv.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.totalTime": {
                "count": 0
            },
            "UPDATE./update/json.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/json.requests": {
                "count": 0
            },
            "UPDATE./update/json.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.totalTime": {
                "count": 0
            },
            "UPDATE./update/json/docs.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/json/docs.requests": {
                "count": 0
            },
            "UPDATE./update/json/docs.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.totalTime": {
                "count": 0
            },
            "UPDATE.update.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE.update.requests": {
                "count": 0
            },
            "UPDATE.update.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.totalTime": {
                "count": 0
            },
            "UPDATE.updateHandler.adds": {
                "value": 0
            },
            "UPDATE.updateHandler.autoCommits": {
                "value": 0
            },
            "UPDATE.updateHandler.commits": {
                "count": 2,
                "meanRate": 0.0000018884883427127664,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateHandler.cumulativeAdds": {
                "count": 11,
                "meanRate": 0.000010386685885140081,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateHandler.cumulativeDeletesById": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.cumulativeDeletesByQuery": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.cumulativeErrors": {
                "count": 1,
                "meanRate": 9.442441713770075e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateHandler.deletesById": {
                "value": 0
            },
            "UPDATE.updateHandler.deletesByQuery": {
                "value": 0
            },
            "UPDATE.updateHandler.docsPending": {
                "value": 0
            },
            "UPDATE.updateHandler.errors": {
                "value": 0
            },
            "UPDATE.updateHandler.expungeDeletes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.merges": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.optimizes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.rollbacks": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.softAutoCommits": {
                "value": 0
            },
            "UPDATE.updateHandler.splits": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            }
        },
        "solr.core.cfxlabs.shard1.replica1": {
            "ADMIN./admin/file.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/file.requests": {
                "count": 0
            },
            "ADMIN./admin/file.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/file.totalTime": {
                "count": 0
            },
            "ADMIN./admin/logging.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/logging.requests": {
                "count": 0
            },
            "ADMIN./admin/logging.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/logging.totalTime": {
                "count": 0
            },
            "ADMIN./admin/luke.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.requestTimes": {
                "count": 19,
                "meanRate": 0.00000987071787580066,
                "1minRate": 2.964393875e-314,
                "5minRate": 6.905094425205174e-110,
                "15minRate": 9.891969587779911e-39,
                "min_ms": 0.076815,
                "max_ms": 9.137404,
                "mean_ms": 4.7982796690630005,
                "median_ms": 9.137404,
                "stddev_ms": 4.506804058833526,
                "p75_ms": 9.137404,
                "p95_ms": 9.137404,
                "p99_ms": 9.137404,
                "p999_ms": 9.137404
            },
            "ADMIN./admin/luke.requests": {
                "count": 19
            },
            "ADMIN./admin/luke.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/luke.totalTime": {
                "count": 11439908
            },
            "ADMIN./admin/mbeans.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.requestTimes": {
                "count": 2,
                "meanRate": 0.0000010390229788766662,
                "1minRate": 2.964393875e-314,
                "5minRate": 6.969250976378221e-111,
                "15minRate": 1.4207756107386616e-39,
                "min_ms": 2.631298,
                "max_ms": 8.187608,
                "mean_ms": 8.187608,
                "median_ms": 8.187608,
                "stddev_ms": 3.673504119314903e-73,
                "p75_ms": 8.187608,
                "p95_ms": 8.187608,
                "p99_ms": 8.187608,
                "p999_ms": 8.187608
            },
            "ADMIN./admin/mbeans.requests": {
                "count": 2
            },
            "ADMIN./admin/mbeans.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/mbeans.totalTime": {
                "count": 10818906
            },
            "ADMIN./admin/ping.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.requestTimes": {
                "count": 23,
                "meanRate": 0.000011948763124178596,
                "1minRate": 2.964393875e-314,
                "5minRate": 8.775503027364883e-110,
                "15minRate": 1.5179976901203948e-38,
                "min_ms": 0.052711,
                "max_ms": 0.866666,
                "mean_ms": 0.12258960007928771,
                "median_ms": 0.076169,
                "stddev_ms": 0.15094404053977653,
                "p75_ms": 0.076169,
                "p95_ms": 0.603791,
                "p99_ms": 0.866666,
                "p999_ms": 0.866666
            },
            "ADMIN./admin/ping.requests": {
                "count": 23
            },
            "ADMIN./admin/ping.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/ping.totalTime": {
                "count": 5035627
            },
            "ADMIN./admin/plugins.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/plugins.requests": {
                "count": 0
            },
            "ADMIN./admin/plugins.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/plugins.totalTime": {
                "count": 0
            },
            "ADMIN./admin/properties.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/properties.requests": {
                "count": 0
            },
            "ADMIN./admin/properties.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/properties.totalTime": {
                "count": 0
            },
            "ADMIN./admin/segments.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.requestTimes": {
                "count": 2,
                "meanRate": 0.000001039022907150586,
                "1minRate": 2.964393875e-314,
                "5minRate": 7.326572114856809e-111,
                "15minRate": 1.4446536350367305e-39,
                "min_ms": 2.027836,
                "max_ms": 9.727703,
                "mean_ms": 9.727703,
                "median_ms": 9.727703,
                "stddev_ms": 0,
                "p75_ms": 9.727703,
                "p95_ms": 9.727703,
                "p99_ms": 9.727703,
                "p999_ms": 9.727703
            },
            "ADMIN./admin/segments.requests": {
                "count": 2
            },
            "ADMIN./admin/segments.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/segments.totalTime": {
                "count": 11755539
            },
            "ADMIN./admin/system.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.requestTimes": {
                "count": 18,
                "meanRate": 0.000009351206743443583,
                "1minRate": 2.964393875e-314,
                "5minRate": 5.04196791616159e-110,
                "15minRate": 7.920102794195676e-39,
                "min_ms": 4.881682,
                "max_ms": 17.523513,
                "mean_ms": 5.3644638008563845,
                "median_ms": 4.881682,
                "stddev_ms": 1.4693622548540755,
                "p75_ms": 4.881682,
                "p95_ms": 9.377451,
                "p99_ms": 11.475604,
                "p999_ms": 11.475604
            },
            "ADMIN./admin/system.requests": {
                "count": 18
            },
            "ADMIN./admin/system.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/system.totalTime": {
                "count": 189471246
            },
            "ADMIN./admin/threads.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/threads.requests": {
                "count": 0
            },
            "ADMIN./admin/threads.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/threads.totalTime": {
                "count": 0
            },
            "ADMIN./config.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.requestTimes": {
                "count": 30,
                "meanRate": 0.00001558534150765813,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 0.462307,
                "max_ms": 57.260466,
                "mean_ms": 13.433358535910559,
                "median_ms": 14.892014,
                "stddev_ms": 11.02642510283997,
                "p75_ms": 17.198104,
                "p95_ms": 28.213062,
                "p99_ms": 57.260466,
                "p999_ms": 57.260466
            },
            "ADMIN./config.requests": {
                "count": 30
            },
            "ADMIN./config.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./config.totalTime": {
                "count": 402952551
            },
            "ADMIN./schema.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./schema.requests": {
                "count": 0
            },
            "ADMIN./schema.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./schema.totalTime": {
                "count": 0
            },
            "CACHE.core.fieldCache": {
                "value": {
                    "entries_count": 0,
                    "total_size": "0 bytes"
                }
            },
            "CACHE.searcher.documentCache": {
                "value": {
                    "lookups": 11530,
                    "evictions": 0,
                    "cumulative_inserts": 10,
                    "cumulative_hits": 11520,
                    "hits": 11520,
                    "cumulative_evictions": 0,
                    "size": 10,
                    "hitratio": 1,
                    "cumulative_lookups": 11530,
                    "cumulative_hitratio": 1,
                    "warmupTime": 0,
                    "inserts": 10
                }
            },
            "CACHE.searcher.fieldValueCache": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.filterCache": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.perSegFilter": {
                "value": {
                    "lookups": 0,
                    "evictions": 0,
                    "cumulative_inserts": 0,
                    "cumulative_hits": 0,
                    "hits": 0,
                    "cumulative_evictions": 0,
                    "size": 0,
                    "hitratio": 0,
                    "cumulative_lookups": 0,
                    "cumulative_hitratio": 0,
                    "warmupTime": 0,
                    "inserts": 0
                }
            },
            "CACHE.searcher.queryResultCache": {
                "value": {
                    "lookups": 761,
                    "evictions": 0,
                    "cumulative_inserts": 2,
                    "cumulative_hits": 760,
                    "hits": 760,
                    "cumulative_evictions": 0,
                    "size": 1,
                    "hitratio": 1,
                    "cumulative_lookups": 762,
                    "cumulative_hitratio": 1,
                    "warmupTime": 0,
                    "inserts": 1
                }
            },
            "CORE.aliases": {
                "value": [
                    "cfxlabs_shard1_replica1"
                ]
            },
            "CORE.collection": {
                "value": "cfxlabs"
            },
            "CORE.coreName": {
                "value": "cfxlabs_shard1_replica1"
            },
            "CORE.fs.totalSpace": {
                "value": 8318783488
            },
            "CORE.fs.usableSpace": {
                "value": 5051539456
            },
            "CORE.indexDir": {
                "value": "/opt/solr/example/cloud/node4/solr/cfxlabs_shard1_replica1/data/index/"
            },
            "CORE.instanceDir": {
                "value": "/opt/solr/example/cloud/node4/solr/cfxlabs_shard1_replica1"
            },
            "CORE.refCount": {
                "value": 1
            },
            "CORE.shard": {
                "value": "shard1"
            },
            "CORE.startTime": {
                "value": "2017-11-28T06:27:10.029Z"
            },
            "INDEX.size": {
                "value": "34.7 KB"
            },
            "INDEX.sizeInBytes": {
                "value": 35531
            },
            "QUERY./browse.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./browse.requests": {
                "count": 0
            },
            "QUERY./browse.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./browse.totalTime": {
                "count": 0
            },
            "QUERY./debug/dump.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./debug/dump.requests": {
                "count": 0
            },
            "QUERY./debug/dump.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./debug/dump.totalTime": {
                "count": 0
            },
            "QUERY./export.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./export.requests": {
                "count": 0
            },
            "QUERY./export.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./export.totalTime": {
                "count": 0
            },
            "QUERY./get.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./get.requests": {
                "count": 0
            },
            "QUERY./get.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./get.totalTime": {
                "count": 0
            },
            "QUERY./graph.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./graph.requests": {
                "count": 0
            },
            "QUERY./graph.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./graph.totalTime": {
                "count": 0
            },
            "QUERY./query.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./query.requests": {
                "count": 0
            },
            "QUERY./query.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./query.totalTime": {
                "count": 0
            },
            "QUERY./select.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.requestTimes": {
                "count": 2693,
                "meanRate": 0.0013990447034304802,
                "1minRate": 2.964393875e-314,
                "5minRate": 5.829192638154585e-97,
                "15minRate": 6.943001418908761e-33,
                "min_ms": 0.08408,
                "max_ms": 93.545816,
                "mean_ms": 3.883961970564557,
                "median_ms": 5.2769,
                "stddev_ms": 3.5548573145502704,
                "p75_ms": 5.778959,
                "p95_ms": 8.382536,
                "p99_ms": 10.619661,
                "p999_ms": 28.127912
            },
            "QUERY./select.requests": {
                "count": 2693
            },
            "QUERY./select.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./select.totalTime": {
                "count": 12442913329
            },
            "QUERY./sql.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./sql.requests": {
                "count": 0
            },
            "QUERY./sql.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./sql.totalTime": {
                "count": 0
            },
            "QUERY./stream.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "QUERY./stream.requests": {
                "count": 0
            },
            "QUERY./stream.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY./stream.totalTime": {
                "count": 0
            },
            "REPLICATION./replication.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.requestTimes": {
                "count": 18,
                "meanRate": 0.00000935120570553141,
                "1minRate": 2.964393875e-314,
                "5minRate": 5.04196791616159e-110,
                "15minRate": 7.920102794195676e-39,
                "min_ms": 0.32958,
                "max_ms": 0.408861,
                "mean_ms": 0.33351079896781993,
                "median_ms": 0.32958,
                "stddev_ms": 0.012954696590517685,
                "p75_ms": 0.32958,
                "p95_ms": 0.349721,
                "p99_ms": 0.408861,
                "p999_ms": 0.408861
            },
            "REPLICATION./replication.requests": {
                "count": 18
            },
            "REPLICATION./replication.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "REPLICATION./replication.totalTime": {
                "count": 8228951
            },
            "REPLICATION.errors": {
                "count": 1
            },
            "REPLICATION.skipped": {
                "count": 0
            },
            "REPLICATION.time": {
                "count": 1,
                "meanRate": 5.195120150174184e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 375.500803,
                "max_ms": 375.500803,
                "mean_ms": 375.500803,
                "median_ms": 375.500803,
                "stddev_ms": 0,
                "p75_ms": 375.500803,
                "p95_ms": 375.500803,
                "p99_ms": 375.500803,
                "p999_ms": 375.500803
            },
            "SEARCHER.new": {
                "count": 7
            },
            "SEARCHER.new.errors": {
                "count": 0
            },
            "SEARCHER.new.maxReached": {
                "count": 0
            },
            "SEARCHER.new.time": {
                "count": 7,
                "meanRate": 0.000003636575951481111,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 8.955284,
                "max_ms": 652.598611,
                "mean_ms": 25.514810515921415,
                "median_ms": 25.494584,
                "stddev_ms": 3.275227180995596,
                "p75_ms": 25.494584,
                "p95_ms": 25.494584,
                "p99_ms": 25.494584,
                "p999_ms": 25.494584
            },
            "SEARCHER.new.warmup": {
                "count": 5,
                "meanRate": 0.000002597554251072206,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 0.032304,
                "max_ms": 1.292459,
                "mean_ms": 0.032304440077229525,
                "median_ms": 0.032304,
                "stddev_ms": 0.00006224877606110415,
                "p75_ms": 0.032304,
                "p95_ms": 0.032304,
                "p99_ms": 0.032304,
                "p999_ms": 0.032304
            },
            "SEARCHER.searcher": {
                "value": {
                    "numDocs": 15,
                    "searcherName": "Searcher@712e966[cfxlabs_shard1_replica1] main",
                    "reader": "ExitableDirectoryReader(UninvertingDirectoryReader(Uninverting(_0(6.6.2):C1) Uninverting(_1(6.6.2):C6) Uninverting(_2(6.6.2):C7) Uninverting(_3(6.6.2):C1)))",
                    "deletedDocs": 0,
                    "registeredAt": "2017-12-08T06:17:39.119Z",
                    "maxDoc": 15,
                    "indexVersion": 14,
                    "warmupTime": 0,
                    "caching": "true",
                    "readerDir": "org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@/opt/solr-6.6.2/example/cloud/node4/solr/cfxlabs_shard1_replica1/data/index lockFactory=org.apache.lucene.store.NativeFSLockFactory@63ac848d; maxCacheMB=48.0 maxMergeSizeMB=4.0)",
                    "openedAt": "2017-12-08T06:17:39.118Z"
                }
            },
            "TLOG.applyingBuffered.ops": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "TLOG.buffered.ops": {
                "value": 0
            },
            "TLOG.replay.ops": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "TLOG.replay.remaining.bytes": {
                "value": 4167
            },
            "TLOG.replay.remaining.logs": {
                "value": 2
            },
            "TLOG.state": {
                "value": 3
            },
            "UPDATE./update.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.requestTimes": {
                "count": 13,
                "meanRate": 0.000006753647398660222,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 9.223999,
                "max_ms": 2080.164557,
                "mean_ms": 698.2489770909392,
                "median_ms": 123.869637,
                "stddev_ms": 578.7426792372404,
                "p75_ms": 1281.328351,
                "p95_ms": 1281.328351,
                "p99_ms": 1281.328351,
                "p999_ms": 1281.328351
            },
            "UPDATE./update.requests": {
                "count": 13
            },
            "UPDATE./update.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update.totalTime": {
                "count": 8501952938
            },
            "UPDATE./update/csv.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/csv.requests": {
                "count": 0
            },
            "UPDATE./update/csv.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/csv.totalTime": {
                "count": 0
            },
            "UPDATE./update/json.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/json.requests": {
                "count": 0
            },
            "UPDATE./update/json.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json.totalTime": {
                "count": 0
            },
            "UPDATE./update/json/docs.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE./update/json/docs.requests": {
                "count": 0
            },
            "UPDATE./update/json/docs.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE./update/json/docs.totalTime": {
                "count": 0
            },
            "UPDATE.update.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE.update.requests": {
                "count": 0
            },
            "UPDATE.update.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.update.totalTime": {
                "count": 0
            },
            "UPDATE.updateHandler.adds": {
                "value": 0
            },
            "UPDATE.updateHandler.autoCommits": {
                "value": 0
            },
            "UPDATE.updateHandler.commits": {
                "count": 4,
                "meanRate": 0.000002078046508982748,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateHandler.cumulativeAdds": {
                "count": 15,
                "meanRate": 0.000007792674482252755,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateHandler.cumulativeDeletesById": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.cumulativeDeletesByQuery": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.cumulativeErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.deletesById": {
                "value": 0
            },
            "UPDATE.updateHandler.deletesByQuery": {
                "value": 0
            },
            "UPDATE.updateHandler.docsPending": {
                "value": 0
            },
            "UPDATE.updateHandler.errors": {
                "value": 0
            },
            "UPDATE.updateHandler.expungeDeletes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.merges": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.optimizes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.rollbacks": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateHandler.softAutoCommits": {
                "value": 2
            },
            "UPDATE.updateHandler.splits": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            }
        },
        "solr.jvm": {
            "buffers.direct.Count": {
                "value": 17
            },
            "buffers.direct.MemoryUsed": {
                "value": 221321
            },
            "buffers.direct.TotalCapacity": {
                "value": 221321
            },
            "buffers.mapped.Count": {
                "value": 136
            },
            "buffers.mapped.MemoryUsed": {
                "value": 1958754
            },
            "buffers.mapped.TotalCapacity": {
                "value": 1958754
            },
            "classes.loaded": {
                "value": 7302
            },
            "classes.unloaded": {
                "value": 50
            },
            "gc.ConcurrentMarkSweep.count": {
                "value": 2
            },
            "gc.ConcurrentMarkSweep.time": {
                "value": 316
            },
            "gc.ParNew.count": {
                "value": 1339
            },
            "gc.ParNew.time": {
                "value": 27729
            },
            "memory.heap.committed": {
                "value": 514523136
            },
            "memory.heap.init": {
                "value": 536870912
            },
            "memory.heap.max": {
                "value": 514523136
            },
            "memory.heap.usage": {
                "value": 0.14510277726364476
            },
            "memory.heap.used": {
                "value": 74658736
            },
            "memory.non-heap.committed": {
                "value": 81129472
            },
            "memory.non-heap.init": {
                "value": 2555904
            },
            "memory.non-heap.max": {
                "value": -1
            },
            "memory.non-heap.usage": {
                "value": -78763360
            },
            "memory.non-heap.used": {
                "value": 78763360
            },
            "memory.pools.CMS-Old-Gen.committed": {
                "value": 402653184
            },
            "memory.pools.CMS-Old-Gen.init": {
                "value": 402653184
            },
            "memory.pools.CMS-Old-Gen.max": {
                "value": 402653184
            },
            "memory.pools.CMS-Old-Gen.usage": {
                "value": 0.06695673863093059
            },
            "memory.pools.CMS-Old-Gen.used": {
                "value": 26960344
            },
            "memory.pools.CMS-Old-Gen.used-after-gc": {
                "value": 14165920
            },
            "memory.pools.Code-Cache.committed": {
                "value": 29622272
            },
            "memory.pools.Code-Cache.init": {
                "value": 2555904
            },
            "memory.pools.Code-Cache.max": {
                "value": 251658240
            },
            "memory.pools.Code-Cache.usage": {
                "value": 0.11611989339192709
            },
            "memory.pools.Code-Cache.used": {
                "value": 29222528
            },
            "memory.pools.Compressed-Class-Space.committed": {
                "value": 5185536
            },
            "memory.pools.Compressed-Class-Space.init": {
                "value": 0
            },
            "memory.pools.Compressed-Class-Space.max": {
                "value": 1073741824
            },
            "memory.pools.Compressed-Class-Space.usage": {
                "value": 0.0044324323534965515
            },
            "memory.pools.Compressed-Class-Space.used": {
                "value": 4759288
            },
            "memory.pools.Metaspace.committed": {
                "value": 46321664
            },
            "memory.pools.Metaspace.init": {
                "value": 0
            },
            "memory.pools.Metaspace.max": {
                "value": -1
            },
            "memory.pools.Metaspace.usage": {
                "value": 0.9667516261937396
            },
            "memory.pools.Metaspace.used": {
                "value": 44781544
            },
            "memory.pools.Par-Eden-Space.committed": {
                "value": 89522176
            },
            "memory.pools.Par-Eden-Space.init": {
                "value": 89522176
            },
            "memory.pools.Par-Eden-Space.max": {
                "value": 89522176
            },
            "memory.pools.Par-Eden-Space.usage": {
                "value": 0.524062685875732
            },
            "memory.pools.Par-Eden-Space.used": {
                "value": 46915232
            },
            "memory.pools.Par-Eden-Space.used-after-gc": {
                "value": 0
            },
            "memory.pools.Par-Survivor-Space.committed": {
                "value": 22347776
            },
            "memory.pools.Par-Survivor-Space.init": {
                "value": 22347776
            },
            "memory.pools.Par-Survivor-Space.max": {
                "value": 22347776
            },
            "memory.pools.Par-Survivor-Space.usage": {
                "value": 0.035044203056268326
            },
            "memory.pools.Par-Survivor-Space.used": {
                "value": 783160
            },
            "memory.pools.Par-Survivor-Space.used-after-gc": {
                "value": 783160
            },
            "memory.total.committed": {
                "value": 595652608
            },
            "memory.total.init": {
                "value": 539426816
            },
            "memory.total.max": {
                "value": 514523135
            },
            "memory.total.used": {
                "value": 153422096
            },
            "os.arch": {
                "value": "amd64"
            },
            "os.availableProcessors": {
                "value": 1
            },
            "os.committedVirtualMemorySize": {
                "value": 2728890368
            },
            "os.freePhysicalMemorySize": {
                "value": 152453120
            },
            "os.freeSwapSpaceSize": {
                "value": 0
            },
            "os.maxFileDescriptorCount": {
                "value": 4096
            },
            "os.name": {
                "value": "Linux"
            },
            "os.openFileDescriptorCount": {
                "value": 184
            },
            "os.processCpuLoad": {
                "value": 0.0017985611510791368
            },
            "os.processCpuTime": {
                "value": 1517830000000
            },
            "os.systemCpuLoad": {
                "value": 0.03776978417266187
            },
            "os.systemLoadAverage": {
                "value": 0
            },
            "os.totalPhysicalMemorySize": {
                "value": 2098753536
            },
            "os.totalSwapSpaceSize": {
                "value": 0
            },
            "os.version": {
                "value": "4.9.38-16.33.amzn1.x86_64"
            },
            "threads.blocked.count": {
                "value": 0
            },
            "threads.count": {
                "value": 26
            },
            "threads.daemon.count": {
                "value": 9
            },
            "threads.deadlock.count": {
                "value": 0
            },
            "threads.deadlocks": {
                "value": []
            },
            "threads.new.count": {
                "value": 0
            },
            "threads.runnable.count": {
                "value": 7
            },
            "threads.terminated.count": {
                "value": 0
            },
            "threads.timed_waiting.count": {
                "value": 11
            },
            "threads.waiting.count": {
                "value": 8
            }
        },
        "solr.node": {
            "ADMIN./admin/authorization.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/authorization.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/authorization.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/authorization.requests": {
                "count": 0
            },
            "ADMIN./admin/authorization.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/authorization.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/authorization.totalTime": {
                "count": 0
            },
            "ADMIN./admin/collections.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/collections.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/collections.requestTimes": {
                "count": 79821,
                "meanRate": 0.041466868044369755,
                "1minRate": 0.20008391368107,
                "5minRate": 0.20115679224487523,
                "15minRate": 0.20065391403064178,
                "min_ms": 0.688626,
                "max_ms": 201.126447,
                "mean_ms": 0.9582829707932914,
                "median_ms": 0.764758,
                "stddev_ms": 0.5007509834138932,
                "p75_ms": 0.813615,
                "p95_ms": 2.157927,
                "p99_ms": 3.265398,
                "p999_ms": 3.265398
            },
            "ADMIN./admin/collections.requests": {
                "count": 79821
            },
            "ADMIN./admin/collections.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/collections.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/collections.totalTime": {
                "count": 73319274875
            },
            "ADMIN./admin/configs.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/configs.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/configs.requestTimes": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/configs.requests": {
                "count": 0
            },
            "ADMIN./admin/configs.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/configs.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/configs.totalTime": {
                "count": 0
            },
            "ADMIN./admin/cores.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.requestTimes": {
                "count": 141,
                "meanRate": 0.00007324925157168932,
                "1minRate": 0.004215212696015613,
                "5minRate": 0.002531936381998376,
                "15minRate": 0.0010137893429325775,
                "min_ms": 0.088804,
                "max_ms": 0.629611,
                "mean_ms": 0.629611,
                "median_ms": 0.629611,
                "stddev_ms": 0,
                "p75_ms": 0.629611,
                "p95_ms": 0.629611,
                "p99_ms": 0.629611,
                "p999_ms": 0.629611
            },
            "ADMIN./admin/cores.requests": {
                "count": 141
            },
            "ADMIN./admin/cores.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.threadPool.parallelCoreAdminExecutor.completed": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.threadPool.parallelCoreAdminExecutor.duration": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "ADMIN./admin/cores.threadPool.parallelCoreAdminExecutor.running": {
                "count": 0
            },
            "ADMIN./admin/cores.threadPool.parallelCoreAdminExecutor.submitted": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/cores.totalTime": {
                "count": 16795278154
            },
            "ADMIN./admin/info.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/info.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/info.requestTimes": {
                "count": 122,
                "meanRate": 0.00006337878404727378,
                "1minRate": 2.964393875e-314,
                "5minRate": 5.5048145523203075e-108,
                "15minRate": 1.155823814351466e-37,
                "min_ms": 3.919166,
                "max_ms": 36.514162,
                "mean_ms": 7.8586230456976764,
                "median_ms": 4.739489,
                "stddev_ms": 5.603296721988371,
                "p75_ms": 16.804698,
                "p95_ms": 16.804698,
                "p99_ms": 16.804698,
                "p999_ms": 16.804698
            },
            "ADMIN./admin/info.requests": {
                "count": 122
            },
            "ADMIN./admin/info.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/info.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/info.totalTime": {
                "count": 1302309595
            },
            "ADMIN./admin/metrics.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/metrics.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/metrics.requestTimes": {
                "count": 77089,
                "meanRate": 0.04004759994236667,
                "1minRate": 0.12015537414868394,
                "5minRate": 0.10413902327942251,
                "15minRate": 0.10138580746235194,
                "min_ms": 1.798468,
                "max_ms": 163.479657,
                "mean_ms": 10.4017620884098,
                "median_ms": 10.417091,
                "stddev_ms": 5.8948826415753866,
                "p75_ms": 12.761215,
                "p95_ms": 14.291967,
                "p99_ms": 45.32443,
                "p999_ms": 45.32443
            },
            "ADMIN./admin/metrics.requests": {
                "count": 77090
            },
            "ADMIN./admin/metrics.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/metrics.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/metrics.totalTime": {
                "count": 442298682092
            },
            "ADMIN./admin/zookeeper.clientErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/zookeeper.errors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/zookeeper.requestTimes": {
                "count": 27,
                "meanRate": 0.000014026450926405605,
                "1minRate": 2.964393875e-314,
                "5minRate": 6.444909612710583e-110,
                "15minRate": 1.0786434094026431e-38,
                "min_ms": 0.648986,
                "max_ms": 33.251213,
                "mean_ms": 14.284258388563396,
                "median_ms": 13.17398,
                "stddev_ms": 3.3646256991703223,
                "p75_ms": 13.17398,
                "p95_ms": 20.078714,
                "p99_ms": 33.251213,
                "p999_ms": 33.251213
            },
            "ADMIN./admin/zookeeper.requests": {
                "count": 27
            },
            "ADMIN./admin/zookeeper.serverErrors": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/zookeeper.timeouts": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "ADMIN./admin/zookeeper.totalTime": {
                "count": 275549420
            },
            "CACHE.fieldCache": {
                "value": {
                    "entries_count": 0,
                    "total_size": "0 bytes"
                }
            },
            "CONTAINER.cores.lazy": {
                "value": 0
            },
            "CONTAINER.cores.loaded": {
                "value": 2
            },
            "CONTAINER.cores.unloaded": {
                "value": 0
            },
            "CONTAINER.fs.totalSpace": {
                "value": 8318783488
            },
            "CONTAINER.fs.usableSpace": {
                "value": 5051539456
            },
            "CONTAINER.threadPool.coreContainerWorkExecutor.completed": {
                "count": 1,
                "meanRate": 5.194979514331766e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "CONTAINER.threadPool.coreContainerWorkExecutor.duration": {
                "count": 1,
                "meanRate": 5.194979514405912e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 0.051894,
                "max_ms": 0.051894,
                "mean_ms": 0.051894,
                "median_ms": 0.051894,
                "stddev_ms": 0,
                "p75_ms": 0.051894,
                "p95_ms": 0.051894,
                "p99_ms": 0.051894,
                "p999_ms": 0.051894
            },
            "CONTAINER.threadPool.coreContainerWorkExecutor.running": {
                "count": 0
            },
            "CONTAINER.threadPool.coreContainerWorkExecutor.submitted": {
                "count": 1,
                "meanRate": 5.194979514243658e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "CONTAINER.threadPool.coreLoadExecutor.completed": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "CONTAINER.threadPool.coreLoadExecutor.duration": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "CONTAINER.threadPool.coreLoadExecutor.running": {
                "count": 0
            },
            "CONTAINER.threadPool.coreLoadExecutor.submitted": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "QUERY.httpShardHandler.availableConnections": {
                "value": 0
            },
            "QUERY.httpShardHandler.http://172.31.45.252:7574/solr/cfxlabs_shard2_replica2/select.post.requests": {
                "count": 1484,
                "meanRate": 0.020044490450344333,
                "1minRate": 2.964393875e-314,
                "5minRate": 3.0008593642151817e-97,
                "15minRate": 3.5654648608962744e-33,
                "min_ms": 0.499706,
                "max_ms": 20.322404,
                "mean_ms": 0.9297839492214802,
                "median_ms": 0.783635,
                "stddev_ms": 0.702069936659158,
                "p75_ms": 1.044385,
                "p95_ms": 1.853063,
                "p99_ms": 4.101323,
                "p999_ms": 5.012648
            },
            "QUERY.httpShardHandler.http://172.31.45.252:7575/solr/cfxlabs_shard1_replica1/select.post.requests": {
                "count": 1153,
                "meanRate": 0.015573651198002064,
                "1minRate": 2.964393875e-314,
                "5minRate": 2.4942062456481483e-97,
                "15minRate": 3.0556886695255875e-33,
                "min_ms": 0.535268,
                "max_ms": 21.527793,
                "mean_ms": 1.1084203108763393,
                "median_ms": 0.636062,
                "stddev_ms": 0.8902798313257375,
                "p75_ms": 1.471739,
                "p95_ms": 4.311329,
                "p99_ms": 4.311329,
                "p999_ms": 4.311329
            },
            "QUERY.httpShardHandler.http://172.31.45.252:8983/solr/cfxlabs_shard1_replica2/select.post.requests": {
                "count": 1169,
                "meanRate": 0.015837452646483077,
                "1minRate": 2.964393875e-314,
                "5minRate": 2.5165222358617856e-97,
                "15minRate": 2.8746265190378136e-33,
                "min_ms": 0.571498,
                "max_ms": 24.117232,
                "mean_ms": 1.2074234075096528,
                "median_ms": 0.90292,
                "stddev_ms": 1.8818781867523187,
                "p75_ms": 1.197804,
                "p95_ms": 2.107755,
                "p99_ms": 2.728027,
                "p999_ms": 24.117232
            },
            "QUERY.httpShardHandler.http://172.31.45.252:8984/solr/cfxlabs_shard2_replica1/select.post.requests": {
                "count": 790,
                "meanRate": 0.01067474319003817,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.7539004286050406e-97,
                "15minRate": 2.073152155403924e-33,
                "min_ms": 0.808669,
                "max_ms": 15.687045,
                "mean_ms": 1.0902100623530209,
                "median_ms": 0.863165,
                "stddev_ms": 0.7285531613502165,
                "p75_ms": 0.950464,
                "p95_ms": 2.604572,
                "p99_ms": 4.665458,
                "p999_ms": 5.942781
            },
            "QUERY.httpShardHandler.leasedConnections": {
                "value": 0
            },
            "QUERY.httpShardHandler.maxConnections": {
                "value": 10000
            },
            "QUERY.httpShardHandler.pendingConnections": {
                "value": 0
            },
            "QUERY.httpShardHandler.threadPool.httpShardExecutor.completed": {
                "count": 4597,
                "meanRate": 0.0023881325486727373,
                "1minRate": 2.964393875e-314,
                "5minRate": 9.73289094708945e-97,
                "15minRate": 1.1554274035555595e-32
            },
            "QUERY.httpShardHandler.threadPool.httpShardExecutor.duration": {
                "count": 4597,
                "meanRate": 0.00238813254870065,
                "1minRate": 2.964393875e-314,
                "5minRate": 9.73289094708945e-97,
                "15minRate": 1.1554274035555595e-32,
                "min_ms": 1.728014,
                "max_ms": 87.753762,
                "mean_ms": 2.8096756114349812,
                "median_ms": 2.711384,
                "stddev_ms": 1.3633757385484764,
                "p75_ms": 3.137472,
                "p95_ms": 3.650697,
                "p99_ms": 6.178473,
                "p999_ms": 25.565297
            },
            "QUERY.httpShardHandler.threadPool.httpShardExecutor.running": {
                "count": 0
            },
            "QUERY.httpShardHandler.threadPool.httpShardExecutor.submitted": {
                "count": 4597,
                "meanRate": 0.0023881325483901313,
                "1minRate": 2.964393875e-314,
                "5minRate": 9.732887908759746e-97,
                "15minRate": 1.1554256735600753e-32
            },
            "UPDATE.updateShardHandler./solr/cfxlabs_shard2_replica2/admin/mbeans.get.requests": {
                "count": 5,
                "meanRate": 0.000054849488914383354,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.611499633280506e-130,
                "15minRate": 2.567310514101279e-45,
                "min_ms": 12.584008,
                "max_ms": 14.960078,
                "mean_ms": 14.960077999999942,
                "median_ms": 14.960078,
                "stddev_ms": 2.702170284075887e-7,
                "p75_ms": 14.960078,
                "p95_ms": 14.960078,
                "p99_ms": 14.960078,
                "p999_ms": 14.960078
            },
            "UPDATE.updateShardHandler.availableConnections": {
                "value": 0
            },
            "UPDATE.updateShardHandler.http://172.31.45.252:8983/solr/cfxlabs_shard1_replica2/get.post.requests": {
                "count": 1,
                "meanRate": 5.195120895486107e-7,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 24.717901,
                "max_ms": 24.717901,
                "mean_ms": 24.717901,
                "median_ms": 24.717901,
                "stddev_ms": 0,
                "p75_ms": 24.717901,
                "p95_ms": 24.717901,
                "p99_ms": 24.717901,
                "p999_ms": 24.717901
            },
            "UPDATE.updateShardHandler.http://172.31.45.252:8983/solr/cfxlabs_shard1_replica2/update.post.requests": {
                "count": 12,
                "meanRate": 0.000011297732048199718,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 2.811507,
                "max_ms": 148.68353,
                "mean_ms": 21.15088103871255,
                "median_ms": 21.14691,
                "stddev_ms": 0.7381725551746869,
                "p75_ms": 21.14691,
                "p95_ms": 21.14691,
                "p99_ms": 21.14691,
                "p999_ms": 21.14691
            },
            "UPDATE.updateShardHandler.leasedConnections": {
                "value": 0
            },
            "UPDATE.updateShardHandler.maxConnections": {
                "value": 100000
            },
            "UPDATE.updateShardHandler.pendingConnections": {
                "value": 0
            },
            "UPDATE.updateShardHandler.threadPool.recoveryExecutor.completed": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateShardHandler.threadPool.recoveryExecutor.duration": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0,
                "min_ms": 0,
                "max_ms": 0,
                "mean_ms": 0,
                "median_ms": 0,
                "stddev_ms": 0,
                "p75_ms": 0,
                "p95_ms": 0,
                "p99_ms": 0,
                "p999_ms": 0
            },
            "UPDATE.updateShardHandler.threadPool.recoveryExecutor.running": {
                "count": 0
            },
            "UPDATE.updateShardHandler.threadPool.recoveryExecutor.submitted": {
                "count": 0,
                "meanRate": 0,
                "1minRate": 0,
                "5minRate": 0,
                "15minRate": 0
            },
            "UPDATE.updateShardHandler.threadPool.updateExecutor.completed": {
                "count": 11,
                "meanRate": 0.000005714478628662438,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            },
            "UPDATE.updateShardHandler.threadPool.updateExecutor.duration": {
                "count": 11,
                "meanRate": 0.000005714478628726639,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313,
                "min_ms": 4.652357,
                "max_ms": 152.370881,
                "mean_ms": 24.8761319102201,
                "median_ms": 24.871855,
                "stddev_ms": 0.731667528626427,
                "p75_ms": 24.871855,
                "p95_ms": 24.871855,
                "p99_ms": 24.871855,
                "p999_ms": 24.871855
            },
            "UPDATE.updateShardHandler.threadPool.updateExecutor.running": {
                "count": 0
            },
            "UPDATE.updateShardHandler.threadPool.updateExecutor.submitted": {
                "count": 11,
                "meanRate": 0.000005714478628594999,
                "1minRate": 2.964393875e-314,
                "5minRate": 1.4821969375e-313,
                "15minRate": 4.44659081257e-313
            }
        }
    }
}