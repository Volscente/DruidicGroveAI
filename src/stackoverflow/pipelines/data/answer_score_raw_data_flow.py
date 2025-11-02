"""
The module implements a Metaflow Pipeline for creating the Raw Data Layer for the StackOverflow
Answer Score Classification use case.
"""

# Import Standard Modules
import os
import logging
from pathlib import Path
from metaflow import FlowSpec, step
from dynaconf import Dynaconf
from stackoverflow.data_preparation.data_preparation import AnswerScoreDataPreparator

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)


class AnswerScoreRawDataFlow(FlowSpec):
    @step
    def start(self):
        """
        Set the root path for the Raw Data Flow.
        """
        logging.info("🏁  Starting AnswerScoreRawDataFlow")

        # Retrieve the root path
        if os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH") is None:
            raise ValueError("🚨  DRUIDIC_GROVE_AI_ROOT_PATH environment variable is not set.")
        else:
            self.root_path = Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
            logging.info(f"🛤️  Root path: {self.root_path}")

        self.next(self.load_configuration)

    @step
    def load_configuration(self):
        """
        Load the configuration for the Raw Data Flow.
        """
        # Read the configuration file
        self.config = Dynaconf(
            settings_files=[
                self.root_path / "configuration" / "stackoverflow" / "raw_data_layer.toml"
            ],
            environments=True,
            env="raw_data_layer",
        ).as_dict()

        # List of tables
        self.raw_tables = list(self.config.keys())

        self.next(self.download_data, foreach="raw_tables")

    @step
    def download_data(self):
        """
        Download the data for the Raw Data layer from each table.
        """
        # Compute file path
        file_path = self.root_path / self.config[self.input]["local_path"]

        # Check if the data are already present, otherwise download them
        if file_path.exists():
            logging.info(f"CSV file {file_path} already exists.")
        else:
            # Instance the Data Preparator
            data_preparator = AnswerScoreDataPreparator()

            # Download the data
            data_preparator._download_raw_data(query_config=self.config[self.input])

        self.next(self.upload_data)

    @step
    def upload_data(self, inputs):
        logging.info(inputs)

        self.next(self.end)

    @step
    def end(self):
        print("✅ StackOverflow Badge Classification raw data created.")


if __name__ == "__main__":
    AnswerScoreRawDataFlow()
