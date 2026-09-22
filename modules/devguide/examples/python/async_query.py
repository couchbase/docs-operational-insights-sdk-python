import asyncio

import utils

cluster = utils.get_asyncio_cluster()

async def main():
    print('======= BASIC QUERY ========')

    # tag::scope-query[]
    scope = cluster.database('travel-sample').scope('inventory')

    query = """
            SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
            FROM route
            GROUP BY airline
            ORDER BY route_count DESC
            """

    res = await scope.execute_query(query)

    print('Rows:')
    async for row in res.rows():
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

    res = await cluster.execute_query(query)
    # end::cluster-query[]

    print(f'Got {len(await res.get_all_rows())} rows')

    print('======= POSITIONAL PARAMETERS ========')

    # tag::query-positional-params[]
    from acouchbase_analytics.options import QueryOptions

    query = """
            SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
            FROM route
            WHERE sourceairport=$1 AND distance>=$2
            GROUP BY airline
            ORDER BY route_count DESC
            """

    res = await scope.execute_query(query, QueryOptions(positional_parameters=['SFO', 1000]))

    # end::query-positional-params[]

    print(f'Got {len(await res.get_all_rows())} rows')

    print('======= NAMED PARAMETERS ========')

    # tag::query-named-params[]
    query = """
            SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
            FROM route
            WHERE sourceairport=$source_airport AND distance>=$min_distance
            GROUP BY airline
            ORDER BY route_count DESC
            """

    res = await scope.execute_query(query, QueryOptions(named_parameters={'source_airport': 'SFO', 'min_distance': 1000}))

    # end::query-named-params[]

    print(f'Got {len(await res.get_all_rows())} rows')


if __name__ == '__main__':
    asyncio.run(main())


