cassandra_host = "cassandra.eu-north-1.amazonaws.com"
cassandra_port = "9142"
user = "nodejs-script-at-211125392861"
password = "Ewy3qUp6abAeoEUdQg10CEx/5PJ+Z53eQTT77pjv1og="
# keyspace = "ctp_data"
# table = "vehicles"

cassandra_options = {
    # "keyspace": keyspace,
    # "table": table,
    "spark.cassandra.connection.host": cassandra_host,
    "spark.cassandra.connection.port": cassandra_port,
    "spark.cassandra.auth.username": user,
    "spark.cassandra.auth.password": password,
}