"""
The module includes Fixtures related to the module "postgresql_connector".
"""

# Import Standard Libraries
import os
import pathlib
from dynaconf import Dynaconf
import pytest

# Import Package Modules
from src.postgresql_connector.postgresql_types import PostgreSQLClientConfig


# Retrieve the root path
root_path = os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH")

# Read the configuration file
config = Dynaconf(
    settings_files=[pathlib.Path(root_path) / "configuration" / "stackoverflow_settings.toml"],
    environments=True,
    env="pytest",
)


@pytest.fixture
def fixture_postgresql_client_config(
    client_config: dict = config["postgresql"]["client"],
) -> PostgreSQLClientConfig:
    """
    Fixture for a PostgreSQLClientConfig object
    from src/postgresql_connector/postgresql_types.py

    Args:
        client_config (Dictionary): Configurations for a PostgreSQLClientConfig object

    Returns:
        (PostgreSQLClientConfig): Object of PostgreSQL client configurations
    """
    return PostgreSQLClientConfig(**client_config)
