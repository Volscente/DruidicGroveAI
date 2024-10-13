"""
Defines the BigqueryConnector class in order to query BigQuery
datasets and tables
"""
# Import Standard Modules
from pathlib import Path

# Import Package Modules
from src.logging_module.logging_module import get_logger


class BigqueryConnector:
    """
    The class implements a BigQuery Connector
    in order to query BigQuery datasets and tables

    Attributes:

    Methods:

    """
    def __init__(self):
        """
        Constructor of the class BigqueryConnector

        Args:

        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 pathlib.Path(__file__).parents[1] /
                                 'logging_module' /
                                 'log_configuration.yaml')

        self.logger.debug('__init__ - Initialise object attributes')

    def _get_client(self):
        # TODO
        pass

    def read_from_query_config(self):
        # TODO
        pass
