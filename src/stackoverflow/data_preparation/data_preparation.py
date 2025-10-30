"""
The module includes classes for implementing data preparation
steps for the StackOverflow use cases.
"""

# Import Standard Modules
import os
import logging
from pathlib import Path
from data_grimorium.bigquery_connector.bigquery_connector import BigQueryConnector
from data_grimorium.bigquery_connector.bigquery_types import (
    BQQueryConfig,
    BQClientConfig,
)


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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

        Args:

        """
        # Initialise attributes
        self._root_path = Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))

    def _download_raw_data(self, raw_data_query: BQQueryConfig) -> None:
        """
        Download raw data from BigQuery and save it to local files.
        """
        # Initialise BigQuery Connector
        connector = BigQueryConnector(
            BQClientConfig(project_id="deep-learning-438509"), root_path=self._root_path
        )

        logging.info(f"📥 Downloading raw data from {raw_data_query.table_name}")

        # Download the raw data
        data = connector.execute_query_from_config(raw_data_query)

        # Local path where to save data
        save_path = self._root_path / raw_data_query.local_path

        logging.info(f"💾 Saving raw data to {save_path}")

        # Write data
        data.to_csv(save_path, index=False)
