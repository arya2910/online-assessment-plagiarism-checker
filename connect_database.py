from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'C:\\Users\\ABC\\projects\\online-assessment-plagiarism-checker-main\\projects\\api\\secure-connect-plagiarism-datasiet.zip'
}
auth_provider = PlainTextAuthProvider('dIOAPeovdKrbZaPepbfTOQFa', 'LpzdH42q9iK5DH00E8.z,GgZzCZc,HAnaG7,crMr7NtkZcD-z-j.vCGxzgJejDhZ79FxBGJZxf3MFKxF9z9_8r7,RDmQi-kW7SDk3SybN2GKAXxNkLC.N.ycytagouAg')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")