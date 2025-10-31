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

        # TODO: Setup BigQuery connector

        # List of tables
        self.raw_tables = list(self.config.keys())

        self.next(self.download_data, foreach="raw_tables")

    @step
    def download_data(self):
        """
        Download the data for the Raw Data layer from each table.
        """
        logging.info(f"📖  Read data for the Raw Table: {self.input.lower()}")

        self.next(self.write_data)

    @step
    def write_data(self, inputs):
        # TODO: the writing has to be done in parallel, this is just for testing.
        print(inputs)
        self.next(self.end)

    @step
    def end(self):
        print("✅ StackOverflow Badge Classification raw data created.")


if __name__ == "__main__":
    AnswerScoreRawDataFlow()
