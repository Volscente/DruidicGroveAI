"""
The module includes tests for the module stackoverflow.data_preparation.
"""

# Import Standard Modules
import pytest
import pandas as pd

# Import Package Modules
from src.stackoverflow.data_preparation.data_preparation import AnswerScoreDataPreparator


@pytest.mark.parametrize(
    "download_query_config, expected_rows",
    [
        (
            {
                "query_path": "data/test/data_preparation/test_download_raw_data_query.sql",
                "table_name": "test_table",
                "local_path": "data/test/test_download_raw_data.csv",
            },
            1,
        )
    ],
)
def test_download_raw_data(
    fixture_answer_score_data_preparator: AnswerScoreDataPreparator,
    download_query_config: dict,
    expected_rows: int,
) -> bool:
    """
    Test the stackoverflow/data_preparation/data_preparation.AnswerScoreDataPreparator.download_raw_data function.

    Args:
        fixture_answer_score_data_preparator (AnswerScoreDataPreparator): Object for data preparation.
        download_query_config (dict): query_path, table_name and local_path where to save .CSV file.
        expected_rows (int): Expected number of rows in the .csv file.
    """
    # Download the data
    fixture_answer_score_data_preparator.download_raw_data(
        download_query_config=download_query_config
    )

    # Read the .csv file
    data = pd.read_csv(
        fixture_answer_score_data_preparator._root_path / download_query_config["local_path"]
    )

    # Check the number of rows
    assert data.shape[0] == expected_rows
