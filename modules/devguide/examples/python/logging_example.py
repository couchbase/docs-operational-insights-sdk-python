#  Copyright 2016-2025. Couchbase, Inc.
#  All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# tag::logging[]
import logging

from couchbase_analytics import LOG_DATE_FORMAT, LOG_FORMAT
from couchbase_analytics.cluster import Cluster
from couchbase_analytics.credential import Credential


# output log messages to example.log
logging.basicConfig(filename='example.log',
                    filemode='w', 
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=LOG_DATE_FORMAT)

logger = logging.getLogger(__name__)
# Good to set the logger's level because if the root level is not set, only WARNING level and above logs are output.
logger.setLevel(logging.DEBUG)


def main() -> None:
    # Update this to your cluster
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)

    # Execute a query and buffer all result rows in client memory.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    res = cluster.execute_query(statement)
    all_rows = res.get_all_rows()
    for row in all_rows:
        logger.info(f'Found row: {row}')
    logger.info(f'metadata={res.metadata()}')

if __name__ == '__main__':
    main()
# end::logging[]
