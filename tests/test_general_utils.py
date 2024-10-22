"""
This test module includes all the tests for the
module src.general_utils.general_utils
"""
# Import Standard Modules
import pathlib
import pytest

# Import Package Modules
from src.general_utils.general_utils import (
    read_file_from_path
)


@pytest.mark.parametrize('input_path, expected_first_line', [
    (pathlib.Path(__file__).parents[1] /
     'queries' /
     'test_queries' /
     'test_access_bigquery_query.sql',
     '/*')
])
def test_read_file_from_path(input_path: pathlib.Path,
                             expected_first_line: str) -> bool:
    """
    Test the function src.general_utils.general_utils.read_file_from_path
    by reading a local file and compare the first line

    Args:
        input_path: pathlib.Path local file path
        expected_first_line: str of file first line

    Returns:
    """

    # Read the file
    file_read = read_file_from_path(input_path)

    assert file_read.partition('\n')[0] == expected_first_line


@pytest.mark.parametrize('input_path, expected_exception', [
    (pathlib.Path(__file__).parents[2] /
     'queries' /
     'test_queries' /
     'wrong_file.sql',
     FileNotFoundError)
])
def test_read_file_from_path_exceptions(
        input_path: pathlib.Path,
        expected_exception: Exception
) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_file_from_path

    Args:
        input_path: pathlib.Path wrong local file path
        expected_exception: Exception instance

    Returns:
    """

    with pytest.raises(expected_exception):
        read_file_from_path(input_path)
