# https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/
from kubernetes import client, config

config.load_kube_config()

v1=client.load_kube_config()
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
