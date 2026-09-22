from couchbase_analytics.cluster import Cluster
from couchbase_analytics.options import ClusterOptions, SecurityOptions
from couchbase_analytics.credential import Credential

from acouchbase_analytics.cluster import AsyncCluster


ENDPOINT = 'https://192.168.107.129:18095'
USERNAME = 'Administrator'
PASSWORD = 'password'


def get_cluster():
    cred = Credential.from_username_and_password(USERNAME, PASSWORD)
    security_options = SecurityOptions(disable_server_certificate_verification=True)
    options = ClusterOptions(security_options=security_options)
    return Cluster.create_instance(ENDPOINT, cred, options)


def get_asyncio_cluster():
    cred = Credential.from_username_and_password(USERNAME, PASSWORD)
    security_options = SecurityOptions(disable_server_certificate_verification=True)
    options = ClusterOptions(security_options=security_options)
    return AsyncCluster.create_instance(ENDPOINT, cred, options)
