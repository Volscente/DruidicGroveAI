"""
The module includes the PostgreSQL connector to interact
with the PostgreSQL database.
"""

# Import Standard Libraries
import os
from pathlib import Path
import psycopg2

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.postgresql_connector.postgresql_types import PostgreSQLClientConfig


class PostgreSQLConnector:
    """
    The class implements a PostgreSQL Connector
    in order to query PostgreSQL datasets and tables.

    Attributes:

    """

    def __init__(self, client_config: PostgreSQLClientConfig):
        """
        Constructor of the class PostgreSQLConnector

        Args:
            client_config (PostgreSQLClientConfig): Config for instance a PostgreSQL Client
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
        self._client_config = client_config

    def _set_client(self):
        """
        Set the attribute ``_client`` with an instance of the PostgreSQL Client.
        """
        self._logger.debug("_set_client - Start")

        self._logger.info("_set_client - Set the PostgreSQL client")

        # Initialise the client
        self._client = psycopg2.connect(*self._client_config)

        # TODO: Check attributes to log
        # TODO: Set the cursor

        self._logger.debug("_set_client - End")
