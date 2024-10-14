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

# Read configuration file
config = Dynaconf(settings_files=[pathlib.Path(__file__).parents[1]
                                  / 'configuration'
                                  / 'settings.toml'],
                  environments=True,
                  env=['pytest'])


@pytest.fixture
def fixture_bigquery_client_config(project_id: str = config['client']['project_id'],
                                   location: str = config['client']['location']) -> BigQueryClientConfig:
    """
    This fixture returns a BigQueryClientConfig object

    Args:
        project_id: String value of the GCP project id
        location: String value of the GCP project location

    Returns:
        client_config: BigQueryClientConfig object
    """
    # Instance a BigQueryClientConfig object
    client_config = BigQueryClientConfig(project_id=project_id,
                                         location=location)

    return client_config


@pytest.fixture
def 
