"""
The module includes Data Preparation class definitions
"""
# Import Standard Libraries
import os
from pathlib import Path

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import BigQueryClientConfig

class StackOverflowDataPreparation:
    """
    The class implements a Data Preparation object for the Stack Overflow
    Answer Score Classification use case

    Attributes:
        logger: logging.Logger object used for logging purposes

    Methods:
    """
    def __init__(self,
                 input_tables_config: dict,
                 bigquery_client_config: BigQueryClientConfig):
        """
        Constructor of the class StackOverflowDataPreparation

        Args:
            input_tables_config: dict with Input Tables (including raw data) configuration
            bigquery_client_config: BigQueryClientConfig including BigQuery client configurations for initialise it
        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                                 'src' /
                                 'logging_module' /
                                 'log_configuration.yaml')

        # Initialise attributes
        self._input_tables_config = input_tables_config

        self.logger.info('__init__ - Start')

        self.logger.info('__init__ - Initialise the BigQueryConnector object')

        # Init a BigQueryConnector object based on the configurations stored in bigquery_client_config
        self.bigquery_connector = BigQueryConnector(bigquery_client_config)

        self.logger.info('__init__ - End')


    def _load_input_tables(self):
        """
        Fetch the input tables in 'self._input_tables_config',
        check if they already exist and, in case not, create them.

        Returns:
        """
        self.logger.info('_load_input_tables - Start')

        self.logger.info('_load_input_tables - Fetch input tables')

        # Fetch input tables stored in the self._input_tables_config
        for input_table in self._input_tables_config:

            self.logger.info('_load_input_tables - Input table: %s', input_table)

            # Check if the table already exist, otherwise create it