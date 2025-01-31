"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest
from dynaconf import Dynaconf

# Import Package Modules
from src.types import BigQueryClientConfig
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
    Fixture for a Dictionary including reading query configurations.
    Parameter configurations structure:
            query_path: <query_local_path>
            query_parameters:
                <parameter_name>:
                    name: <parameter_name>
                    type: <parameter_bigquery_type>
                    value: <parameter_value>

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        query_config (Dictionary): Query configurations
    """

    return query_config


@pytest.fixture
def fixture_create_table_query_config(
        query_config: dict = config['create_table_query_config']
) -> dict:
    """
    Fixture for a Dictionary including creating table query configurations.
    Parameter configurations structure:
            query_path: <query_local_path>
            query_parameters:
                <parameter_name>:
                    name: <parameter_name>
                    type: <parameter_bigquery_type>
                    value: <parameter_value>

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        query_config (Dictionary): Query configurations
    """

    return query_config


@pytest.fixture
def fixture_stackoverflow_data_preparation(
        fixture_bigquery_client_config: BigQueryClientConfig,
        dataset_name: str = config['data_preparation']['dataset_name'],
        input_tables_config: dict = config['data_preparation']['input_tables']
) -> StackOverflowDataPreparation:
    """
    Fixture for a StackOverflowDataPreparation object
    from src/data_preparation/data_preparation.StackOverflowDataPreparation class definition.

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations for a BigQueryConnector object
        dataset_name (String): Dataset name
        input_tables_config (Dictionary): Input table query configurations

    Returns:
        stackoverflow_data_preparation (StackOverflowDataPreparation): Object for data preparation
    """

    # Instance a StackOverflowDataPreparation object
    stackoverflow_data_preparation = StackOverflowDataPreparation(
        dataset_name=dataset_name,
        input_tables_config=input_tables_config,
        bigquery_client_config=fixture_bigquery_client_config
    )

    return stackoverflow_data_preparation
