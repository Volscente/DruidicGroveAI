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
    Test the function
    src/bigquery_connector/bigquery_connector.BigQueryConnector._set_client
    by instantiating a BigQueryConnector object and check the "client" attribute

    Args:
        fixture_bigquery_connector: BigQueryConnector object

    Returns:
    """
    # Retrieve credentials
    credentials = fixture_bigquery_connector.client._credentials

    assert credentials is not None
