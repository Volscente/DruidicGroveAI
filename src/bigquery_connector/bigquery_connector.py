"""
Defines the BigqueryConnector class in order to query BigQuery
datasets and tables
"""
# Import Standard Modules
from google.cloud import bigquery
from pathlib import Path

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import BigQueryClientConfig


class BigQueryConnector:
    """
    The class implements a BigQuery Connector
    in order to query BigQuery datasets and tables

    Attributes:
        client_config: BigQueryClientConfig including all necessary variables for instance a BigQuery Client instance

    Methods:

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
        self.logger = get_logger(__class__.__name__,
                                 Path(__file__).parents[1] /
                                 'logging_module' /
                                 'log_configuration.yaml')

        self.logger.debug('__init__ - Initialise object attributes')

        # Initialise attributes
        self.client_config = client_config

        # Set the client
        self._set_client()

    def _set_client(self):
        """
        Set the attribute 'client' with an instance of the BigQuery Client

        Returns:
            client: bigquery.Client object
        """
        self.logger.debug('_set_client - Start')

        self.logger.info('_set_client - Set the BigQuery client')

        # Set the client
        self.client = bigquery.Client(
            project=self.client_config.project_id,
            location=self.client_config.location
        )

        self.logger.debug('_set_client - End')

    def read_from_query_config(self):
        # TODO
        pass
