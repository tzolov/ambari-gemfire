export SERVICE=GEODE
export PASSWORD=admin
export AMBARI_HOST=c6401.ambari.apache.org
export CLUSTER=ambari_geode

curl -u admin:$PASSWORD -i -H 'X-Requested-By: PDE' -X PUT -d '{"RequestInfo": {"context" :"Stop GEODE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE
curl -u admin:$PASSWORD -i -H 'X-Requested-By: PDE' -X DELETE http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

rm -rf /opt/pivotal/*
