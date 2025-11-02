"""
The module includes classes for implementing data preparation
steps for the StackOverflow use cases.
"""

# Import Standard Modules
import os
import logging
from pathlib import Path
from data_grimorium.bigquery_connector.bigquery_connector import BigQueryConnector
from data_grimorium.bigquery_connector.bigquery_types import BQClientConfig
from data_grimorium.postgresql_connector.postgresql_connector import PostgreSQLConnector
from data_grimorium.postgresql_connector.postgresql_types import PostgreSQLClientConfig


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)


class AnswerScoreDataPreparator:
    """
    The class implements a Data Preparator for the
    StackOverflow Answer Score Classification
    use case.

    Attributes:
        _raw_data_queries (List[BQQueryConfig]): List of raw data queries to download
        _root_path (Path): Root path of the package

    Methods:
    """

    def __init__(self):
        """
        Initialize the class.
        """
        # Initialise attributes
        self._root_path = Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))

        # Initialise BigQuery Connector
        self._bigquery_connector = BigQueryConnector(
            BQClientConfig(project_id=os.getenv("PROJECT_ID")), root_path=self._root_path
        )

        # Initialise PostgreSQL Connector
        self.postgres_connector = PostgreSQLConnector(
            client_config=PostgreSQLClientConfig(
                dbname=os.getenv("POSTGRESQL_DB"),
                user=os.getenv("POSTGRESQL_USER"),
                password=os.getenv("POSTGRESQL_PASSWORD"),
                host=os.getenv("POSTGRESQL_HOST"),
                port=os.getenv("POSTGRESQL_PORT"),
            ),
            root_path=self._root_path,
        )

    def download_raw_data(self, query_config: dict) -> None:
        """
        Download raw data from BigQuery and save it to local files.

        Args:
            query_config (dict): Query configuration for the raw data to download and upload to PostgreSQL.
        """
        # Wrap dictionary to query parameters
        raw_data_query_config = self._bigquery_connector.wrap_dictionary_to_query_config(
            query_config
        )

        logging.info(f"📥 Downloading raw data from {raw_data_query_config.table_name}")

        # Download the raw data
        data = self._bigquery_connector.execute_query_from_config(raw_data_query_config)

        # Local path where to save data
        save_path = self._root_path / raw_data_query_config.local_path

        logging.info(f"💾 Saving raw data to {save_path}")

        # Write data
        data.to_csv(save_path, index=False)

    def upload_raw_data(self) -> None:
        """
        Upload raw data to PostgreSQL.

        Args:

        Returns:

        """
