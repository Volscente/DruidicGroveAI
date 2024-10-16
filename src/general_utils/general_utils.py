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

    logger.info('read_file_from_path - Start')

    # Check if the file_path exists
    if file_path.exists():

        logger.info('read_file_from_path - Reading file from %s', file_path.as_posix())

        # Read file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_read = file.read()
    else:
        raise FileNotFoundError(f'Unable to locate file: {file_path.as_posix()}')

    logger.info('read_file_from_path - Successfully file read from %s', file_path.as_posix())

    logger.info('read_file_from_path - Start')

    return file_read
