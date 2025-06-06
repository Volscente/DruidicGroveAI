"""
Defines the BigqueryConnector class in order to query BigQuery
datasets and tables
"""

# Import Standard Modules
import os
from pathlib import Path
from typing import Union, List
import pandas as pd
from google.cloud import bigquery

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.custom_types import BigQueryClientConfig, BigQueryQueryParameter, BigQueryQueryConfig
from src.general_utils.general_utils import read_file_from_path


class BigQueryConnector:
    """
    The class implements a BigQuery Connector
    in order to query BigQuery datasets and tables

    Attributes:
        _logger (logging.Logger): Object used for logging purposes
        _client_config (BigQueryClientConfig): Configurations for instance a BigQuery Client instance
        _client (bigquery.Client): BigQuery client object
    """

    def __init__(self, client_config: BigQueryClientConfig):
        """
        Constructor of the class BigqueryConnector

        Args:
            client_config (BigQueryClientConfig):  Config for
                           instance a BigQuery Client
        """
        # Setup logger
        self._logger = get_logger(
            __class__.__name__,
            Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
            / "src"
            / "logging_module"
            / "log_configuration.yaml",
        )

        self._logger.debug("__init__ - Initialise object attributes")

        # Initialise attributes
        self._client_config = client_config

        # Set the client
        self._set_client()

    def _set_client(self):
        """
        Set the attribute ``_client`` with an instance of the BigQuery Client

        Returns:
            Set ``_client`` BigQuery Client object
        """
        self._logger.debug("_set_client - Start")

        self._logger.info("_set_client - Set the BigQuery client")

        # Set the client
        self._client = bigquery.Client(
            project=self._client_config.project_id,
        )

        self._logger.debug("_set_client - End")

    def _build_query_parameters(
        self, query_parameters: List[BigQueryQueryParameter]
    ) -> List[Union[bigquery.ArrayQueryParameter, bigquery.ScalarQueryParameter]]:
        """
        Build BigQuery query parameters from an object BigQueryQueryParameter

        Args:
            query_parameters (List[BigQueryQueryParameter]): Query parameters

        Returns:
            bigquery_query_parameters (List[Union[bigquery.ArrayQueryParameter, bigquery.ScalarQueryParameter]]):
            BigQuery list of parameters
        """

        self._logger.debug("build_bigquery_query_parameters_from_dictionary - Start")

        # Initialise empty list BigQuery query parameters
        bigquery_query_parameters = []

        self._logger.info(
            "build_bigquery_query_parameters_from_dictionary - Fetch BigQuery query parameters"
        )

        # Fetch all query parameters
        for query_parameter in query_parameters:
            # Check if the ScalarQueryParameter or ArrayQueryParameter is required
            # The difference is in the type of values passed (No list: scalar, list: array)
            if isinstance(query_parameter.value, list):
                # Build the parameter
                bigquery_parameter = bigquery.ArrayQueryParameter(
                    *query_parameter.__dict__.values()
                )
            else:
                # Build the parameter
                bigquery_parameter = bigquery.ScalarQueryParameter(
                    *query_parameter.__dict__.values()
                )

            # Append to the list of parameters
            bigquery_query_parameters.append(bigquery_parameter)

        self._logger.info(
            "build_bigquery_query_parameters_from_dictionary - Successfully built BigQuery query parameters"
        )

        self._logger.debug("build_bigquery_query_parameters_from_dictionary - End")

        return bigquery_query_parameters

    def execute_query_from_config(
        self, query_config: BigQueryQueryConfig
    ) -> Union[pd.DataFrame, bool]:
        """
        Execute a query from local path and with a certain set of parameter configurations.
        The query can either read data or create a table on BigQuery.

        Args:
            query_config (BigQueryQueryConfig): Query configurations (path and parameters)

        Returns:
            result (Union[pd.DataFrame, bool]): The result of the query execution.

                  - pd.DataFrame: When the query is executed successfully and returns data.

                  - bool: `True` if the query executes successfully but does not return data
        """
        self._logger.debug("execute_query_from_config - Start")

        # Initialise result to return
        result = None

        # Retrieve query path
        query_path = Path(query_config.query_path)

        self._logger.info(
            "execute_query_from_config - Reading query file: %s", query_path.as_posix()
        )

        # Read query
        query = read_file_from_path(query_path)

        # Check if there are parameters
        if query_config.query_parameters is None:
            self._logger.info("execute_query_from_config - Querying BigQuery without Parameters")

            # Execute the job in BigQuery
            job = self._client.query(query)

        else:
            # Retrieve BigQuery query parameters
            parameters = self._build_query_parameters(query_config.query_parameters)

            self._logger.info("execute_query_from_config - Querying BigQuery with Parameters")

            # Execute the job BigQuery with parameters
            job = self._client.query(
                query=query,
                job_config=bigquery.QueryJobConfig(query_parameters=parameters),
            )

        self._logger.info("execute_query_from_config - Successfully query executed")

        # Extract the job result
        result = job.result()

        # Switch between a read query and a table creation query
        if job.statement_type == "CREATE_TABLE_AS_SELECT":
            self._logger.info("execute_query_from_config - Created table from query")

            # Return table creation status
            # NOTE: Using the 'job.done()' does not return True unless few time has passed
            result = job.done()

        else:
            self._logger.info("execute_query_from_config - Converting data to Pandas DataFrame")

            # Convert data to a Pandas DataFrame
            result = result.to_dataframe()

        self._logger.debug("execute_query_from_config - End")

        return result

    def table_exists(self, table_name: str, dataset_name: str) -> bool:
        """
        Check if a table exists in a dataset

        Args:
            table_name (String): Name of the table
            dataset_name (String): Name of the dataset

        Returns:
            exists (Boolean): Flag indicating if the table exists
        """
        self._logger.info("table_exists - Start")

        self._logger.info("table_exists - Retrieve list of tables for dataset: %s", dataset_name)

        # Retrieve list of tables
        tables = self._client.list_tables(dataset_name)

        # Retrieve list of table names
        table_names = [table.table_id for table in tables]

        # Check if the table exist
        exists = table_name in table_names

        self._logger.info("table_exists - Table %s exists: %s", table_name, exists)

        self._logger.info("table_exists - End")

        return exists

    def wrap_dictionary_to_query_config(self, query_config_dictionary: dict) -> BigQueryQueryConfig:
        """
        Converts a dictionary of Query Configurations into a ``BigQueryQueryConfig`` object.

        Args:
            query_config_dictionary (dict): The dictionary containing Query Configurations.

        Returns:
            (BigQueryQueryConfig): Object with BigQuery query configurations.
        """
        self._logger.info("wrap_dictionary_to_query_parameters - Start")

        # Check if there are parameters
        if "query_parameters" not in query_config_dictionary.keys():
            self._logger.info("wrap_dictionary_to_query_parameters - No query parameters")
        else:
            self._logger.info("wrap_dictionary_to_query_parameters - Wrapping query parameters")

            # Retrieve parameters
            query_parameters = query_config_dictionary["query_parameters"]

            # Wrap query parameters
            wrapped_parameters = [
                BigQueryQueryParameter(**query_parameters[parameter])
                for parameter in query_parameters
            ]

            # Update the dictionary with the wrapped parameters
            query_config_dictionary["query_parameters"] = wrapped_parameters

        return BigQueryQueryConfig(**query_config_dictionary)
