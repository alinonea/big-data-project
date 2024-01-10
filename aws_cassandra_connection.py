from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2 , CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

ssl_context = SSLContext(PROTOCOL_TLSv1_2 )
ssl_context.load_verify_locations('./sf-class2-root.crt')
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username='nodejs-script-at-211125392861', password='Ewy3qUp6abAeoEUdQg10CEx/5PJ+Z53eQTT77pjv1og=')
cluster = Cluster(['cassandra.eu-north-1.amazonaws.com'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142)
session = cluster.connect()
r = session.execute('select * from ctp_data.vehicles')