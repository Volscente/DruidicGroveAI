"""
The module contains several general util functions with no
specific technology or SDK binding (e.g., Google SDK)
"""
# Import Standard Libraries
import os
import pathlib


# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def read_file_from_path(file_path: pathlib.Path) -> str:
    """
    Read a file from local path

    Args:
        file_path: pathlib.Path local file path

    Returns:
        file_read: str read file
    """

    logger.debug('read_file_from_path - Start')

    # Retrieve root directory path
    # TODO: Check test test_read_from_query_config
    root_path = pathlib.Path(os.getenv('PYTHONPATH'))

    logger.debug('read_file_from_path - Root directory: %s', root_path.as_posix())

    # Update the file_path with the project root directory
    file_path = root_path / file_path

    # Check if the file_path exists
    if file_path.exists():

        logger.info('read_file_from_path - Reading file from %s', file_path.as_posix())

        # Read file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_read = file.read()
    else:
        raise FileNotFoundError(f'Unable to locate file: {file_path.as_posix()}')

    logger.info('read_file_from_path - Successfully file read from %s', file_path.as_posix())

    logger.debug('read_file_from_path - End')

    return file_read
