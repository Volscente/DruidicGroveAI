"""
This test module includes all the tests for the
module src.bigquery_connector
"""
# Import Standard Libraries
from google.cloud import bigquery
import pytest

# Import Package Modules
from src.bigquery_connector.bigquery_connector import BigQueryConnector


@pytest.mark.skip(
    reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
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
    credentials = fixture_bigquery_connector._client._credentials

    assert credentials is not None


@pytest.mark.skip(
    reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
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
    Test the function src/bigquery_connector/bigquery_connector.BigQueryConnector._build_query_parameters
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


@pytest.mark.skip(
    reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
@pytest.mark.parametrize('index, expected_id, expected_display_name', [
    (0, 3863, 'Adam Hughes'),
])
def test_read_from_query_config(fixture_bigquery_connector: BigQueryConnector,
                                fixture_query_config: dict,
                                index: int,
                                expected_id: int,
                                expected_display_name: str) -> bool:
    """
    Test the function
    src/bigquery_connector/bigquery_connector.BigQueryConnector._read_from_query_config
    by reading the data from BigQuery and comparing them with expected values

    Args:
        fixture_bigquery_connector: BigQueryConnector object
        fixture_query_config: Dictionary of query configurations
        index: Integer DataFrame row index
        expected_id: Integer DataFrame for row 'id' value
        expected_display_name: String DataFrame for row 'display_name' value

    Returns:
    """
    # Read data
    data = fixture_bigquery_connector.read_from_query_config(query_config=fixture_query_config)

    # Retrieve id and display_name
    row_id, row_display_name = data.loc[index, 'id'], data.loc[index, 'display_name']

    assert expected_id == row_id and expected_display_name == row_display_name
