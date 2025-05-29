"""
This test module includes all the tests for the
module src.logging_module.logging_module
"""

# Import Standard Modules
import pathlib
import pytest

# Import Package Modules
from logging_module.logging_module import get_logger


@pytest.mark.parametrize(
    "input_logger, input_config_path, expected_name",
    [
        (
            "general_utils",
            pathlib.Path(__file__).parents[1]
            / "src"
            / "logging_module"
            / "log_configuration.yaml",
            "general_utils",
        ),
    ],
)
def test_get_logger(
    input_logger: str, input_config_path: pathlib.Path, expected_name: str
) -> bool:
    """
    Test the function src/logging_module/logging_module.get_logger

    Args:
        input_logger (String): Logger name
        input_config_path (pathlib.Path): Local file path to the logging configuration
        expected_name (String): Expected logger name
    """

    # Retrieve the logger
    logger = get_logger(input_logger, input_config_path)

    assert logger.name == expected_name


@pytest.mark.parametrize(
    "input_logger, input_config_path, expected_exception",
    [
        (
            "general_utils",
            pathlib.Path(__file__).parents[1]
            / "src"
            / "logging_module"
            / "wrong_log_configuration.yaml",
            FileNotFoundError,
        ),
    ],
)
def test_get_logger_exceptions(
    input_logger: str, input_config_path: pathlib.Path, expected_exception: Exception
) -> bool:
    """
    Test the exceptions trigger by the
    function src/logging_module/logging_module.get_logger

    Args:
        input_logger (String): Logger name
        input_config_path (pathlib.Path): Local wrong file path to the logging configuration
        expected_exception (Exception): Expected triggered exception
    """

    with pytest.raises(expected_exception):
        get_logger(input_logger, input_config_path)
