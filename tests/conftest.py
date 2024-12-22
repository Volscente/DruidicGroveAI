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
                                  / 'settings.toml'],
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
def fixture_dictionary_query_parameters(query_config: dict = config['query_config']['query_parameters']):
    """
    Fixture for a Dictionary Query Parameter with structure:
        name: <name_of_the_query_parameter>
        array_type: <type_of_the_parameter>
        value: <value_of_the_parameter>

    Args:
        query_config: Dictionary of query parameters

    Returns:
        query_parameters: Dictionary of query parameters
    """

    return query_config


@pytest.fixture
def fixture_query_config(
        query_config: dict = config['query_config']
) -> dict:
    # TODO: Rename the configuration in the "settings.toml" file
    # TODO: Rename the fixture
    # TODO: Modify the docstring
    """
    Fixture for a Dictionary Query Configurations with structure:
        query_path: <path_of_the_query_file>
        query_parameters:
            name: <name_of_the_query_parameter>
            array_type: <type_of_the_parameter>
            value: <value_of_the_parameter>

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
    Fixture for a Dictionary Query Configurations that creates a table.
    Configuration Structure:
        query_path: <path_of_the_query_file>
        query_parameters:
            name: <name_of_the_query_parameter>
            array_type: <type_of_the_parameter>
            value: <value_of_the_parameter>

    Args:
        query_config: Dictionary query configuration

    Returns:
        query_config: Dictionary of query configurations
    """
    # TODO: Implement
    pass