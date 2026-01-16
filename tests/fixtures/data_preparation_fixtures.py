"""
The module includes Fixtures related to the modules
like "data_preparation".
"""

# Import Standard Modules
import pytest

# Import Package Modules
from src.stackoverflow.data_preparation.data_preparation import AnswerScoreDataPreparator


@pytest.fixture
def fixture_answer_score_data_preparator():
    """
    Fixture for the AnswerScoreDataPreparator class.
    """
    return AnswerScoreDataPreparator()
