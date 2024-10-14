"""
This test module includes all the tests for the
module src.bigquery_connector
"""
# Import Standard Libraries
import pytest

# Import Package Modules
from src.bigquery_connector.bigquery_connector import BigQueryConnector


def test_set_client(fixture_bigquery_connector: BigQueryConnector) -> bool:
    """

    Args:
        fixture_bigquery_connector:

    Returns:

    """
    # TODO: Add test
    print(fixture_bigquery_connector.client)

    assert True