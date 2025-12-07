"""
The module includes classes for implementing data preparation
steps for the StackOverflow use cases.
"""

# Import Standard Modules
import os
import logging
import pandas as pd
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
    The class implements a Data Preparator for the StackOverflow Answer Score
    Classification use case. It includes functions for downloading the raw data,
    upload them into a dedicated PostgreSQL database and transform the data in order to
    make them ready for the model training.

    Attributes:
        _raw_data_queries (List[BQQueryConfig]): List of raw data queries to download
        _root_path (Path): Root path of the package

    Methods:
        download_raw_data: Download raw data from BigQuery and save it to local .csv files.
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

    def download_raw_data(self, download_query_config: dict) -> None:
        """
        Download raw data from BigQuery and save it to local .csv files.

        Args:
            download_query_config (dict): query_path, table_name and local_path where to save .CSV file.
        """
        # Wrap dictionary to query parameters
        raw_data_query_config = self._bigquery_connector.wrap_dictionary_to_query_config(
            download_query_config
        )

        logging.info(f"📥 Downloading raw data from {raw_data_query_config.table_name}")

        # Download the raw data
        data = self._bigquery_connector.execute_query_from_config(raw_data_query_config)

        # Local path where to save data
        save_path = self._root_path / raw_data_query_config.local_path

        logging.info(f"💾 Saving raw data to {save_path}")

        # Write data
        data.to_csv(save_path, index=False)

    def upload_raw_data(self, upload_query_config: dict) -> None:
        """
        Upload raw data to PostgreSQL from local .csv files.

        Args:
            upload_query_config (dict): Local paths to the .csv files.
        """
        logging.info(f"🚀 Uploading raw data into table {upload_query_config['table_name']}")

        # Check if the table already exists
        if not self.postgres_connector.table_exists(upload_query_config["table_name"]):
            # Full path to .csv file
            file_path = self._root_path / upload_query_config["local_path"]

            logging.info(f"📖 Reading from {file_path.as_posix()}")

            # Read data
            data_to_upload = pd.read_csv(file_path)

            # Upload data
            self.postgres_connector.upload_dataframe(
                data=data_to_upload, table_name=upload_query_config["table_name"], replace=False
            )
