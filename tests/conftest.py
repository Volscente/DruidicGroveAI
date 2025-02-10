"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest
from dynaconf import Dynaconf
from typing import List

# Import Package Modules
from src.types import (
    BigQueryClientConfig,
    BigQueryQueryConfig
)
from src.bigquery_connector.bigquery_connector import BigQueryConnector
from src.data_preparation.data_preparation import StackOverflowDataPreparation

# Read configuration file
config = Dynaconf(settings_files=[pathlib.Path(__file__).parents[1]
                                  / 'configuration'
                                  / 'stackoverflow_settings.toml'],
                  environments=True,
                  env='pytest')


@pytest.fixture
def fixture_bigquery_client_config(
        project_id: str = config['client']['project_id']
) -> BigQueryClientConfig:
    """
    This fixture returns a BigQueryClientConfig object

    Args:
        project_id (String): GCP project id

    Returns:
        client_config (BigQueryClientConfig): BigQuery object
    """
    # Instance a BigQueryClientConfig object
    client_config = BigQueryClientConfig(project_id=project_id)

    return client_config


@pytest.fixture
def fixture_bigquery_connector(
        fixture_bigquery_client_config: BigQueryClientConfig
) -> BigQueryConnector:
    """
    This fixture returns a BigQueryConnector object

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations of BigQuery client

    Returns:
        bigquery_connector (BigQueryConnector): BigQuery Connector object
    """
    # Instance a BigQueryConnector object
    bigquery_connector = BigQueryConnector(client_config=fixture_bigquery_client_config)

    return bigquery_connector


@pytest.fixture
def fixture_read_query_config(
        query_config: dict = config['read_query_config']
) -> dict:
    """
    Fixture for a BigQueryQueryConfig read query configobject

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """

    return BigQueryQueryConfig(**query_config)


@pytest.fixture
def fixture_create_table_query_config(
        query_config: dict = config['create_table_query_config']
) -> dict:
    """
    Fixture for a BigQueryQueryConfig create table query config object

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """

    return BigQueryQueryConfig(**query_config)


@pytest.fixture
def fixture_input_table_configs(
        input_tables_config: dict = config['data_preparation']['input_tables']
) -> List[BigQueryQueryConfig]:
    """
    Fixture for providing the input table configurations required for testing or running
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
def fixture_raw_dataset_config(
        query_config: dict = config['data_preparation']['raw_dataset']
) -> BigQueryQueryConfig:
    """
    Fixture for a BigQueryQueryConfig object including the Test Raw Dataset configurations
    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """
    return BigQueryQueryConfig(**query_config)


@pytest.fixture
def fixture_stackoverflow_data_preparation(
        fixture_bigquery_client_config: BigQueryClientConfig,
        fixture_input_table_configs: List[BigQueryQueryConfig],
        fixture_raw_dataset_config: BigQueryQueryConfig,
        dataset_name: str = config['data_preparation']['dataset_name'],
) -> StackOverflowDataPreparation:
    """
    Fixture for a StackOverflowDataPreparation object
    from src/data_preparation/data_preparation.StackOverflowDataPreparation class definition.

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations for a BigQueryConnector object
        fixture_input_table_configs (List[BigQueryQueryConfig]): Input table configurations
        fixture_raw_dataset_config (BigQueryQueryConfig): Configurations for a BigQueryQueryConfig object for raw dataset
        dataset_name (String): Dataset name

    Returns:
        stackoverflow_data_preparation (StackOverflowDataPreparation): Object for data preparation
    """

    # Instance a StackOverflowDataPreparation object
    stackoverflow_data_preparation = StackOverflowDataPreparation(
        dataset_name=dataset_name,
        input_tables_configs=fixture_input_table_configs,
        raw_dataset_config=fixture_raw_dataset_config,
        bigquery_client_config=fixture_bigquery_client_config
    )

    return stackoverflow_data_preparation
