curl --user admin:admin -H 'X-Requested-By:Pivotal' -X POST http://c6401.ambari.apache.org:8080/api/v1/blueprints/blueprint-geode-3-node -d @blueprint-geode-3-node.json

curl --user admin:admin -H 'X-Requested-By:Pivotal' -X POST http://c6401.ambari.apache.org:8080/api/v1/clusters/geode_ambari -d @hostmapping-geode-3-node.json
