"""
This test module includes all the tests for the
module src.types
"""
# Import Standard Libraries
import pytest
from pydantic import ValidationError

# Import Package Modules
from src.types import (
    BigQueryQueryParameter,
    BigQueryQueryConfig
)


@pytest.mark.parametrize('name, parameter_type, value', [
    ('test_name', 'test_type', 'test_value)')
])
def test_bigquery_query_parameter(
        name: str,
        parameter_type: str,
        value: str
) -> bool:
    """
    Test the class BigQueryQueryParameter

    Args:
        name: (String) Parameter name
        parameter_type: (String) Parameter type
        value: (String) The value of the parameter

    Returns:
    """
    # Create a BigQueryQueryParameter object
    bigquery_query_parameter = BigQueryQueryParameter(name=name,
                                                      type=parameter_type,
                                                      value=value)

    assert bigquery_query_parameter.name == name
    assert bigquery_query_parameter.type == parameter_type
    assert bigquery_query_parameter.value == value

@pytest.mark.parametrize('name, value', [
    ('test_name', 'test_value)')
])
def test_bigquery_query_parameter_exceptions(
        name: str,
        value: str
) -> bool:
    """
    Test the class BigQueryQueryParameter for exceptions

    Args:
        name: (String) Parameter name
        value: (String) The value of the parameter

    Returns:
    """
    # Create a BigQueryQueryParameter object without the 'type' attributes
    with pytest.raises(ValidationError):
        BigQueryQueryParameter(name=name,
                               value=value)
