"""
The module contains several general util functions with no
specific technology or SDK binding (e.g., Google SDK)
"""
# Import Standard Libraries
import os
import pathlib
import yaml

# Import Package Modules
from logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def read_configuration(file_name: str) -> dict:
    """
    Read and return the specified configuration file from the 'configuration' folder

    Args:
        file_name: String configuration file name to read

    Returns:
        configuration: Dictionary configuration
    """

    logger.info('read_configuration - Start')

    try:

        logger.info('read_configuration - Reading %s', file_name)

        # Read configuration file
        with open(pathlib.Path(__file__).parents[2] / 'configuration' / file_name,
                  encoding='utf-8') as config_file:

            configuration = yaml.safe_load(config_file.read())

    except FileNotFoundError as exc:

        raise FileNotFoundError(f'read_data - File {file_name} not found') from exc

    logger.info('read_configuration - Successfully configuration file read from %s', file_name)

    logger.info('read_configuration - End')

    return configuration


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
