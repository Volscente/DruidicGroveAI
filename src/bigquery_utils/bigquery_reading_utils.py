"""
The module contains several reading util functions
for reading datasets & tables from BigQuery
"""
# Import Standard Libraries
import os
import pathlib
import pandas as pd
from google.cloud import bigquery


# Import Package Modules
from general_utils.general_utils import read_file_from_path
from logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def read_bq_from_query(query_path: pathlib.Path,
                       client: bigquery.Client,
                       parameters: bigquery.ArrayQueryParameter = None) -> pd.DataFrame:
    """
    Read the query from local path and retrieve data from BigQuery

    Args:
        query_path: pathlib.Path local query file
        client: bigquery.Client BigQuery client for connection
        parameters: bigquery.ArrayQueryParameter query parameters, default=None

    Returns
        data: pd.DataFrame retrieved data
    """
    logger.info('read_bq_from_query - Start')
    logger.info('read_bq_from_query - Reading query file: %s', query_path.as_posix())

    # Read local query file
    query = read_file_from_path(query_path)

    # Check if there are parameters
    if parameters is None:

        logger.info('read_bq_from_query - Querying BigQuery without Parameters')

        # Read data from BigQuery
        data = client.query(query)

    else:

        logger.info('read_bq_from_query - Querying BigQuery without Parameters')

        # Read data from BigQuery with parameters
        data = client.query(query,
                            job_config=bigquery.QueryJobConfig(query_parameters=parameters))

    logger.info('read_bq_from_query - Successfully retrieve data')

    logger.info('read_bq_from_query - End')

    return data.to_dataframe()
