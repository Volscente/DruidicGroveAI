"""
This test module includes all the tests for the
module src.types
"""
# Import Standard Libraries
import pytest
from pydantic import ValidationError
from typing import Tuple

# Import Package Modules
from src.types import (
    BigQueryQueryParameter,
    BigQueryQueryConfig
)


@pytest.mark.parametrize('name, parameter_type, value', [
    ('test_name', 'test_type', 'test_value')
])
def test_bigquery_query_parameter(
        name: str,
        parameter_type: str,
        value: str
) -> bool:
    """
    Test the class BigQueryQueryParameter

    Args:
        name (String): Parameter name
        parameter_type (String): Parameter type
        value (String): Value of the parameter

    Returns:
    """
    # Create a BigQueryQueryParameter object
    bigquery_query_parameter = BigQueryQueryParameter(name=name,
                                                      type=parameter_type,
                                                      value=value)

    assert bigquery_query_parameter.name == name
    assert bigquery_query_parameter.type == parameter_type
    assert bigquery_query_parameter.value == value


# noinspection PyArgumentList
@pytest.mark.parametrize('name, value', [
    ('test_name', 'test_value')
])
def test_bigquery_query_parameter_exceptions(
        name: str,
        value: str
) -> bool:
    """
    Test the class BigQueryQueryParameter for exceptions

    Args:
        name (String): Parameter name
        value (String): Value of the parameter

    Returns:
    """
    # Create a BigQueryQueryParameter object without the 'type' attributes
    with pytest.raises(ValidationError):
        BigQueryQueryParameter(name=name,
                               value=value)


@pytest.mark.parametrize('query_path, query_parameters, local_path', [
    ('test_query_path', ('test_name', 'test_type', 'test_value'), 'test_local_path')
])
def test_bigquery_query_config(
        query_path: str,
        query_parameters: Tuple[str, str, str],
        local_path: str) -> bool:
    """
    Test the class BigQueryQueryConfig

    Args:
        query_path (String): Query file path
        query_parameters (Tuple[str, str, str]): List of BigQuery parameters
        local_path (String): Local path where to save the data

    Returns:
    """
    # Create the BigQueryQueryParameter object
    bigquery_query_parameter = BigQueryQueryParameter(name=query_parameters[0],
                                                      type=query_parameters[1],
                                                      value=query_parameters[2])

    # Create the BigQueryQueryConfig object
    bigquery_query_config = BigQueryQueryConfig(query_path=query_path,
                                                query_parameters=[bigquery_query_parameter],
                                                local_path=local_path)

    assert bigquery_query_config.query_path == query_path
    assert bigquery_query_config.query_parameters[0].name == query_parameters[0]
    assert bigquery_query_config.query_parameters[0].type == query_parameters[1]
    assert bigquery_query_config.query_parameters[0].value == query_parameters[2]
    assert bigquery_query_config.local_path == local_path


# noinspection PyArgumentList
@pytest.mark.parametrize('query_path, query_parameters', [
    ('test_query_path', ('test_name', 'test_type', 'test_value'))
])
def test_bigquery_query_config_exceptions(query_path: str,
                                          query_parameters: Tuple[str, str, str]) -> bool:
    """
    Test the class BigQueryQueryConfig for exceptions

    Args:
        query_path (String): Query file path
        query_parameters (Tuple[str, str, str]): List of BigQuery parameters

    Returns:
    """
    # Test for missing local_path
    bigquery_query_parameter = BigQueryQueryParameter(
        name=query_parameters[0],
        type=query_parameters[1],
        value=query_parameters[2]
    )
    with pytest.raises(ValidationError):
        BigQueryQueryConfig(query_path=query_path,
                            query_parameters=[bigquery_query_parameter])
