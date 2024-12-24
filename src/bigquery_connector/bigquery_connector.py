"""
Defines the BigqueryConnector class in order to query BigQuery
datasets and tables
"""
# Import Standard Modules
import os
from pathlib import Path
import pandas as pd
from google.cloud import bigquery
from typing import Union

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import BigQueryClientConfig
from src.general_utils.general_utils import (
    read_file_from_path
)


class BigQueryConnector:
    """
    The class implements a BigQuery Connector
    in order to query BigQuery datasets and tables

    Attributes:
        logger: logging.Logger object used for logging purposes
        client_config: BigQueryClientConfig including all necessary variables for instance a BigQuery Client instance

    Methods:
        _set_client: Set the attribute 'client' with an instance of the BigQuery Client
        _build_query_parameters: Build BigQuery query parameters from a dictionary in which each key is a BigQuery Parameter
        read_from_query_config: Read the query from local path and retrieve data from BigQuery
    """
    def __init__(self,
                 client_config: BigQueryClientConfig):
        """
        Constructor of the class BigqueryConnector

        Args:
            client_config: BigQueryClientConfig including all necessary variables for
                           instance a BigQuery Client instance
        """
        # Setup logger
        self._logger = get_logger(__class__.__name__,
                                 Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                                 'src' /
                                 'logging_module' /
                                 'log_configuration.yaml')

        self._logger.debug('__init__ - Initialise object attributes')

        # Initialise attributes
        self._client_config = client_config

        # Set the client
        self._set_client()

    def _set_client(self):
        """
        Set the attribute 'client' with an instance of the BigQuery Client

        Returns:
            client: bigquery.Client object
        """
        self._logger.debug('_set_client - Start')

        self._logger.info('_set_client - Set the BigQuery client')

        # Set the client
        self._client = bigquery.Client(
            project=self._client_config.project_id,
        )

        self._logger.debug('_set_client - End')

    def _build_query_parameters(self,
                                query_parameters: dict) -> list:
        """
        Build BigQuery query parameters from a dictionary in which each key
        is a BigQuery Parameter like:
            name: <name_of_the_query_parameter>
            array_type: <type_of_the_parameter>
            value: <value_of_the_parameter>

        Args:
            query_parameters: dict parameters

        Returns
            bigquery_query_parameters: list BigQuery query parameters
        """

        self._logger.debug('build_bigquery_query_parameters_from_dictionary - Start')

        # Initialise empty list BigQuery query parameters
        bigquery_query_parameters = []

        self._logger.info('build_bigquery_query_parameters_from_dictionary - Fetch BigQuery query parameters')

        # Fetch all query parameters
        for query_parameter_key in query_parameters.keys():

            # Check if the ScalarQueryParameter or ArrayQueryParameter is required
            # The difference is in the type of values passed (No list: scalar, list: array)
            if isinstance(query_parameters[query_parameter_key]['value'], list):

                # Build the parameter
                bigquery_parameter = bigquery.ArrayQueryParameter(
                    query_parameters[query_parameter_key]['name'],
                    query_parameters[query_parameter_key]['type'],
                    query_parameters[query_parameter_key]['value']
                )
            else:
                # Build the parameter
                bigquery_parameter = bigquery.ScalarQueryParameter(
                    query_parameters[query_parameter_key]['name'],
                    query_parameters[query_parameter_key]['type'],
                    query_parameters[query_parameter_key]['value']
                )
            # Append to the list of parameters
            bigquery_query_parameters.append(bigquery_parameter)

        self._logger.info('build_bigquery_query_parameters_from_dictionary - Successfully built BigQuery query parameters')

        self._logger.debug('build_bigquery_query_parameters_from_dictionary - End')

        return bigquery_query_parameters

    def execute_query_from_config(self,
                                  query_config: dict) -> Union[pd.DataFrame, int]:
        """
        Execute a query from local path and with a certain set of parameter configurations

        Args:
            query_config: Dictionary query configurations (path and parameters)

        Returns
            data: pd.DataFrame retrieved data
        """
        # TODO: Check response if there is a flag indicating table creation successful
        # TODO: Modify the return to switch between read data and table creation
        self._logger.debug('read_from_query_config - Start')

        # Retrieve query path
        query_path = Path(query_config['query_path'])

        self._logger.info('read_from_query_config - Reading query file: %s',
                         query_path.as_posix())

        # Read query
        query = read_file_from_path(query_path)

        # Check if there are parameters
        if 'query_parameters' not in query_config.keys():

            self._logger.info('read_from_query_config - Querying BigQuery without Parameters')

            # Read data from BigQuery
            data = self._client.query(query)

        else:

            # Retrieve BigQuery query parameters
            parameters = self._build_query_parameters(query_config['query_parameters'])

            self._logger.info('read_from_query_config - Querying BigQuery with Parameters')

            # Read data from BigQuery with parameters
            data = self._client.query(query=query,
                                      job_config=bigquery.QueryJobConfig(query_parameters=parameters))

        self._logger.info('read_from_query_config - Successfully retrieve data')
        self._logger.info('read_from_query_config - Converting data to Pandas DataFrame')

        # Convert data to a Pandas DataFrame
        data = data.to_dataframe()

        self._logger.debug('read_from_query_config - End')

        return data
