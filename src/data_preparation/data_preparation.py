"""
The module includes Data Preparation class definitions
"""
# Import Standard Libraries
import os
from pathlib import Path

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import BigQueryClientConfig
from src.bigquery_connector.bigquery_connector import BigQueryConnector

class StackOverflowDataPreparation:
    """
    The class implements a Data Preparation object for the Stack Overflow
    Answer Score Classification use case

    Attributes:
        _logger: logging.Logger object used for logging purposes
        _input_tables_config: Dictionary with input table configurations
        _dataset_name: Name of the dataset to use
        _bigquery_connector: BigQueryConnector object for interacting with BigQuery


    Methods:
    """
    def __init__(self,
                 input_tables_config: dict,
                 dataset_name: str,
                 bigquery_client_config: BigQueryClientConfig):
        """
        Constructor of the class StackOverflowDataPreparation

        Args:
            input_tables_config: dict with Input Tables (including raw data) configuration
            dataset_name: Name of the dataset to use
            bigquery_client_config: BigQueryClientConfig including BigQuery client configurations for initialise it
        """
        # Setup logger
        self._logger = get_logger(__class__.__name__,
                                 Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                                 'src' /
                                 'logging_module' /
                                 'log_configuration.yaml')

        # Initialise attributes
        self._input_tables_config = input_tables_config
        self._dataset_name = dataset_name

        self._logger.info('__init__ - Start')

        self._logger.info('__init__ - Initialise the BigQueryConnector object')

        # Init a BigQueryConnector object based on the configurations stored in bigquery_client_config
        self._bigquery_connector = BigQueryConnector(bigquery_client_config)

        self._logger.info('__init__ - End')


    def _load_input_tables(self):
        """
        Fetch the input tables in 'self._input_tables_config',
        check if they already exist and, in case not, create them.

        Returns:
        """
        self._logger.info('_load_input_tables - Start')

        self._logger.info('_load_input_tables - Fetch input tables')

        # Fetch input tables stored in the self._input_tables_config
        for input_table in self._input_tables_config.keys():

            self._logger.info('_load_input_tables - Input table: %s', input_table)

            # Switch if table exists or not
            if self._bigquery_connector.table_exists(table_name=input_table, dataset_name=self._dataset_name):
                self._logger.info('_load_input_tables - Input table already exists')
            else:
                self._logger.info('_load_input_tables - Input table does not exist')

                # Create input table
                self._bigquery_connector.execute_query_from_config(self._input_tables_config[input_table])

        self._logger.info('__load_input_tables - Input tables successfully created')

        self._logger.info('__load_input_tables - End')

# TODO: I need to understand how to make the class StackOverflowDataPreparation suitable
# for a local run and a Metaflow pipeline.
# Maybe define all the steps as functions, then another function like "run_pipeline_locally".
# In this function it will call all the other functions.
# For the Metaflow pipeline, each @step will call the "step" function and never call the
# "run_pipeline_locally".
