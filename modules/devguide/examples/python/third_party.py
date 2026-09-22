import utils

cluster = utils.get_cluster()
scope = cluster.database('travel-sample').scope('inventory')

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        GROUP BY airline
        ORDER BY route_count DESC
        """

print('====== Pandas example ======')

# tag::pandas[]
import pandas as pd

res = scope.execute_query(query)
df = pd.DataFrame.from_records(res.rows(), index='airline')

print(df.head())
#          route_count  avg_route_distance
# airline
# AA              2354         2314.884359
# UA              2180         2350.365407
# DL              1981         2350.494112
# US              1960         2101.417609
# WN              1146         1397.736500

# end::pandas[]

print('====== PyArrow example ======')

# tag::pyarrow[]
import pyarrow as pa

res = scope.execute_query(query)
table = pa.Table.from_pylist(res.get_all_rows())

print(table.to_string())
# pyarrow.Table
# route_count: int64
# avg_route_distance: double
# airline: string
# end::pyarrow[]
