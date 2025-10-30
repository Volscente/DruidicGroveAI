"""
The module implements a Metaflow Pipeline for creating the Raw Data Layer for the StackOverflow
Answer Score Classification use case.
"""

# Import Standard Modules
import os
import logging
from pathlib import Path
from metaflow import FlowSpec, step

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)


class AnswerScoreRawDataFlow(FlowSpec):
    @step
    def start(self):
        logging.info("🏁  Starting AnswerScoreRawDataFlow")

        # Retrieve the root path
        if os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH") is None:
            raise ValueError("🚨  DRUIDIC_GROVE_AI_ROOT_PATH environment variable is not set.")
        else:
            self.root_path = Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
            logging.info(f"🛤️  Root path: {self.root_path}")

        self.next(self.end)

    # @step
    # def load_configuration(self):
    #     # Read the configuration file
    #     config = Dynaconf(
    #         settings_files=[root_path / "configuration" / "datagrimorium_settings.toml"],
    #         environments=True,
    #         env="pytest",
    #     )

    @step
    def end(self):
        print("✅ StackOverflow Badge Classification raw data created.")


if __name__ == "__main__":
    AnswerScoreRawDataFlow()
