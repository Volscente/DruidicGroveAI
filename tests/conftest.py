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
        project_id: String value of the GCP project id

    Returns:
        client_config: BigQueryClientConfig object
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
        fixture_bigquery_client_config: BigQueryClientConfig object for instancing a BigQuery client

    Returns:
        bigquery_connector: BigQueryConnector object
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
        query_config: Dictionary of query configurations

    Returns:
        query_config: Dictionary of query configurations
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
        query_config: Dictionary query configuration

    Returns:
        query_config: Dictionary of query configurations
    """

    return query_config
