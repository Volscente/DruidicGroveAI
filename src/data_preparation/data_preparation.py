"""
The module includes Data Preparation class definitions
"""
# Import Standard Libraries
import os
from pathlib import Path

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import (
    BigQueryClientConfig,
    BigQueryQueryConfig
)
from src.bigquery_connector.bigquery_connector import BigQueryConnector

class StackOverflowDataPreparation:
    """
    The class implements a Data Preparation object for the Stack Overflow
    Answer Score Classification use case

    Attributes:
        _logger (logging.Logger): Object used for logging purposes
        _input_tables_config (Dictionary): Input table configurations
        _dataset_name (String): Dataset name to use
        _raw_dataset_config (BigQueryQueryConfig): Raw dataset configurations
        _bigquery_connector (BigQueryConnector): Object for interacting with BigQuery


    Methods:
    """
    def __init__(self,
                 input_tables_config: dict,
                 dataset_name: str,
                 raw_dataset_config: BigQueryQueryConfig,
                 bigquery_client_config: BigQueryClientConfig):
        """
        Constructor of the class StackOverflowDataPreparation

        Args:
            input_tables_config (Dictionary): Input Tables (including raw data) configuration
            dataset_name (String): Name of the dataset to use
            bigquery_client_config (BigQueryClientConfig): BigQuery client configurations for initialise it
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
        self._raw_dataset_config = raw_dataset_config

        self._logger.info('__init__ - Start')

        self._logger.info('__init__ - Initialise the BigQueryConnector object')

        # Init a BigQueryConnector object based on the configurations stored in bigquery_client_config
        self._bigquery_connector = BigQueryConnector(bigquery_client_config)

        # Load the input tables
        self._load_input_tables()

        # Load the raw dataset
        self._load_raw_dataset()

        self._logger.info('__init__ - End')


    def _load_input_tables(self) -> None:
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
                self._logger.info('_load_input_tables - Input table %s already exists', input_table)
            else:
                self._logger.info('_load_input_tables - Input table does not exist')

                # Create input table
                self._bigquery_connector.execute_query_from_config(self._input_tables_config[input_table])

        self._logger.info('__load_input_tables - Input tables successfully created')

        self._logger.info('__load_input_tables - End')


    def _load_raw_dataset(self) -> None:
        """
        Loads the raw dataset into BigQuery. This function is designed to handle
        the initial ingestion of raw data and store it for further processing.

        Returns:
        """
        self._logger.info('_load_raw_dataset - Start')

        self._logger.info('_load_raw_dataset - Load raw dataset')

        # Switch if raw dataset exists or not
        if self._bigquery_connector.table_exists(table_name='raw_dataset', dataset_name=self._dataset_name):
            self._logger.info('_load_raw_dataset - Raw dataset already exists')
        else:
            self._logger.info('_load_raw_dataset - Raw dataset does not exist')

            # Create raw dataset
            self._bigquery_connector.execute_query_from_config(self._raw_dataset_config)

        self._logger.info('_load_raw_dataset - End')
