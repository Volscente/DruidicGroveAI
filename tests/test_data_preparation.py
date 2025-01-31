"""
This test module includes all the tests for the
module src.data_preparation
"""
# Import Standard Libraries
import pytest

# Import Package Modules
from src.data_preparation.data_preparation import StackOverflowDataPreparation

@pytest.mark.skip(
   reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
def test_load_input_tables(
        fixture_stackoverflow_data_preparation: StackOverflowDataPreparation
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation.StackOverflowDataPreparation._load_input_tables

    Args:
        fixture_stackoverflow_data_preparation (StackOverflowDataPreparation): Object for data preparation

    Returns:
    """

    # Load input tables
    fixture_stackoverflow_data_preparation._load_input_tables()

    assert True
