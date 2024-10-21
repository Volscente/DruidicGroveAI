"""
This test module includes all the tests for the
module src.bigquery_connector
"""
# Import Standard Libraries
from google.cloud import bigquery
import pytest

# Import Package Modules
from src.bigquery_connector.bigquery_connector import BigQueryConnector


def test_set_client(
        fixture_bigquery_connector: BigQueryConnector
) -> bool:
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


@pytest.mark.parametrize('bigquery_parameter', [
    (bigquery.ScalarQueryParameter(name='id', type_='INTEGER', value=3863)),
    (bigquery.ScalarQueryParameter(name='display_name', type_='STRING', value='Adam Hughes'))
])
def test_build_query_parameters(
        fixture_bigquery_connector: BigQueryConnector,
        fixture_dictionary_query_parameters: dict,
        bigquery_parameter: bigquery.ScalarQueryParameter
) -> bool:
    """
    Test the function src.bigquery_connector.bigquery_connector.BigQueryConnector._build_query_parameters
    by checking if the test bigquery_parameter is among the built ones

    Args:
        fixture_bigquery_connector: BigQueryConnector object
        fixture_dictionary_query_parameters: Dictionary of query parameters
        bigquery_parameter: bigquery.ScalarQueryParameter BigQuery Parameter

    Returns:
    """

    # Built BigQuery parameters
    built_bigquery_parameters = fixture_bigquery_connector._build_query_parameters(
        query_parameters=fixture_dictionary_query_parameters
    )

    assert bigquery_parameter in built_bigquery_parameters
