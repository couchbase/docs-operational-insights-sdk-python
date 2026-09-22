import utils

cluster = utils.get_cluster()

print('======= BASIC QUERY ========')

# tag::scope-query[]
scope = cluster.database('travel-sample').scope('inventory')

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query)

print('Rows:')
for row in res.rows():
    print(row)

print(f'\nMetadata: {res.metadata()}')
# end::scope-query[]

print('======= CLUSTER-LEVEL QUERY ========')

# tag::cluster-query[]
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM `travel-sample`.inventory.route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = cluster.execute_query(query)
# end::cluster-query[]

print(f'Got {len(list(res.rows()))} rows')

print('======= POSITIONAL PARAMETERS ========')

# tag::query-positional-params[]
from couchbase_analytics.options import QueryOptions

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$1 AND distance>=$2
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query, QueryOptions(positional_parameters=['SFO', 1000]))

# end::query-positional-params[]

print(f'Got {len(list(res.rows()))} rows')

print('======= NAMED PARAMETERS ========')

# tag::query-named-params[]
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$source_airport AND distance>=$min_distance
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query, QueryOptions(named_parameters={'source_airport': 'SFO', 'min_distance': 1000}))

# end::query-named-params[]

print(f'Got {len(list(res.rows()))} rows')
