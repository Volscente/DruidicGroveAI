"""
The module includes Data Preparation class definitions
"""

# Import Standard Libraries
import os
from pathlib import Path
from typing import List

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import BigQueryClientConfig, BigQueryQueryConfig
from src.bigquery_connector.bigquery_connector import BigQueryConnector


class StackOverflowDataPreparation:
    """
    The class implements a Data Preparation object for the Stack Overflow
    Answer Score Classification use case

    Attributes:
        _logger (logging.Logger): Object used for logging purposes
        _input_tables_configs (List[BigQueryQueryConfig]): Input table configurations
        _dataset_name (String): Dataset name to use
        _raw_dataset_config (BigQueryQueryConfig): Raw dataset configurations
        _bigquery_connector (BigQueryConnector): Object for interacting with BigQuery
    """

    def __init__(
        self,
        input_tables_configs: List[BigQueryQueryConfig],
        dataset_name: str,
        raw_dataset_config: BigQueryQueryConfig,
        bigquery_client_config: BigQueryClientConfig,
    ):
        """
        Constructor of the class StackOverflowDataPreparation

        Args:
            input_tables_configs (List[BigQueryQueryConfig]): Input Tables (including raw data) configurations
            dataset_name (String): Name of the dataset to use
            raw_dataset_config (BigQueryQueryConfig): Raw dataset configurations
            bigquery_client_config (BigQueryClientConfig): BigQuery client configurations for initialise it
        """
        # Setup logger
        self._logger = get_logger(
            __class__.__name__,
            Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
            / "src"
            / "logging_module"
            / "log_configuration.yaml",
        )

        # Initialise attributes
        self._input_tables_configs = input_tables_configs
        self._dataset_name = dataset_name
        self._raw_dataset_config = raw_dataset_config

        self._logger.debug("__init__ - Start")

        self._logger.info("__init__ - Initialise the BigQueryConnector object")

        # Init a BigQueryConnector object based on the configurations stored in bigquery_client_config
        self._bigquery_connector = BigQueryConnector(bigquery_client_config)

        self._logger.debug("__init__ - End")

    def _load_input_tables(self) -> None:
        """
        Fetch the input tables in ``self._input_tables_configs``,
        check if they already exist and, in case not, create them.

        Returns:
            Create the input tables in BigQuery
        """
        self._logger.debug("_load_input_tables - Start")

        self._logger.info("_load_input_tables - Fetch input tables")

        # Fetch input tables stored in the self._input_tables_configs
        for input_table_config in self._input_tables_configs:
            # Retrieve table name
            table_name = input_table_config.table_name

            self._logger.info("_load_input_tables - Input table: %s", table_name)

            # Switch if table exists or not
            if self._bigquery_connector.table_exists(
                table_name=table_name, dataset_name=self._dataset_name
            ):
                self._logger.info("_load_input_tables - Input table %s already exists", table_name)
            else:
                self._logger.info("_load_input_tables - Input table does not exist")

                # Create input table
                self._bigquery_connector.execute_query_from_config(input_table_config)

        self._logger.info("__load_input_tables - Input tables successfully created")

        self._logger.debug("__load_input_tables - End")

    def _load_raw_dataset(self) -> None:
        """
        Loads the raw dataset into BigQuery. This function is designed to handle
        the initial ingestion of raw data and store it for further processing.

        Returns:
            Create the raw dataset in BigQuery
        """
        self._logger.debug("_load_raw_dataset - Start")

        self._logger.info("_load_raw_dataset - Load raw dataset")

        # Switch if the raw dataset exists or not
        if self._bigquery_connector.table_exists(
            table_name="raw_dataset", dataset_name=self._dataset_name
        ):
            self._logger.info("_load_raw_dataset - Raw dataset already exists")
        else:
            self._logger.info("_load_raw_dataset - Raw dataset does not exist")

            # Create raw dataset
            self._bigquery_connector.execute_query_from_config(self._raw_dataset_config)

        self._logger.debug("_load_raw_dataset - End")
