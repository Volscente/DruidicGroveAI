"""
The module includes functions for implementing data transformations
"""
# Import Standard Libraries
import os
import pathlib


# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                    'src' /
                    'logging_module' /
                    'log_configuration.yaml')