"""
The module includes Fixtures related to the module "data_preparation".
"""

# Import Standard Libraries
import os
import pathlib
import pytest
from dynaconf import Dynaconf
from typing import List

# Import Package Modules
from src.custom_types import BigQueryClientConfig, BigQueryQueryConfig
from src.data_preparation.data_preparation import StackOverflowBigQueryDataPreparation

# Retrieve the root path
root_path = os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH")

# Read the configuration file
config = Dynaconf(
    settings_files=[pathlib.Path(root_path) / "configuration" / "stackoverflow_settings.toml"],
    environments=True,
    env="pytest",
)


@pytest.fixture
def fixture_bigquery_input_table_configs(
    input_tables_config: dict = config["bigquery"]["data_preparation"]["input_tables"],
) -> List[BigQueryQueryConfig]:
    """
    Fixture for providing the input table configurations in BigQuery required for testing or running
    data preparation pipelines.

    Args:
        input_tables_config (Dictionary): The configuration dictionary containing details of
            input tables required for data preparation.

    Returns:
        config_list (List[BigQueryQueryConfig]): List of BigQueryQueryConfig objects representing the input tables.
    """
    # Initialise the list
    config_list = []

    # Fetch the input table configs
    for table in input_tables_config:
        # Retrieve table config
        table_config = input_tables_config[table]

        # Create the BigQuery config
        bigquery_query_config = BigQueryQueryConfig(**table_config)

        # Add to the list
        config_list.append(bigquery_query_config)

    return config_list


@pytest.fixture
def fixture_bigquery_raw_dataset_config(
    query_config: dict = config["bigquery"]["data_preparation"]["raw_dataset"],
) -> BigQueryQueryConfig:
    """
    Fixture for a BigQueryQueryConfig object including the Test Raw Dataset configurations
    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as an object
    """
    return BigQueryQueryConfig(**query_config)


@pytest.fixture
def fixture_stackoverflow_bigquery_data_preparation(
    fixture_bigquery_client_config: BigQueryClientConfig,
    fixture_bigquery_input_table_configs: List[BigQueryQueryConfig],
    fixture_bigquery_raw_dataset_config: BigQueryQueryConfig,
    dataset_name: str = config["bigquery"]["data_preparation"]["dataset_name"],
) -> StackOverflowBigQueryDataPreparation:
    """
    Fixture for a StackOverflowBigQueryDataPreparation object
    from src/data_preparation/data_preparation.StackOverflowBigQueryDataPreparation class definition.

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations for a BigQueryConnector object
        fixture_bigquery_input_table_configs (List[BigQueryQueryConfig]): Input table configurations
        fixture_bigquery_raw_dataset_config (BigQueryQueryConfig): Configurations for a BigQueryQueryConfig object for raw dataset
        dataset_name (String): Dataset name

    Returns:
        stackoverflow_data_preparation (StackOverflowBigQueryDataPreparation): Object for data preparation
    """

    # Instance a StackOverflowBigQueryDataPreparation object
    stackoverflow_data_preparation = StackOverflowBigQueryDataPreparation(
        dataset_name=dataset_name,
        input_tables_configs=fixture_bigquery_input_table_configs,
        raw_dataset_config=fixture_bigquery_raw_dataset_config,
        bigquery_client_config=fixture_bigquery_client_config,
    )

    return stackoverflow_data_preparation
