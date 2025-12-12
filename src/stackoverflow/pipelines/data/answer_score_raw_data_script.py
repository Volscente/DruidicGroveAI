"""
The module includes the script to create the
Raw Data layer for the use case StackOverflow
Answer Score Classification.
"""

# Import Standard Modules
import os
import logging
from dynaconf import Dynaconf
from pathlib import Path

# Import Package Modules
from stackoverflow.data_preparation.data_preparation import AnswerScoreDataPreparator


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)

# Retrieve the root path
if os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH") is None:
    raise ValueError("🚨 DRUIDIC_GROVE_AI_ROOT_PATH environment variable is not set.")
else:
    root_path = Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
    logging.info(f"🛤️ Root path: {root_path}")

# Read the configuration file
config = Dynaconf(
    settings_files=[root_path / "configuration" / "stackoverflow" / "raw_data_layer.toml"],
    environments=True,
    env="raw_data_layer",
).as_dict()

# Instance the Data Preparator
data_preparator = AnswerScoreDataPreparator()

# Loop over the raw data tables
for raw_data_config in config:
    logging.info(f" 🚀Uploading {raw_data_config} data")

    # Compute file path
    file_path = root_path / config[raw_data_config]["local_path"]

    # Check if the data are already present, otherwise download them
    if file_path.exists():
        logging.info(f"⏭️ .csv file {file_path} already exists.")
    else:
        # Download the data
        data_preparator.download_raw_data(download_query_config=config[raw_data_config])

    # Upload the data
    data_preparator.upload_raw_data(upload_query_config=config[raw_data_config])
