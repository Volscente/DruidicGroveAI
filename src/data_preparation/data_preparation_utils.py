"""
The module includes functions for implementing data transformations
"""
# Import Standard Libraries
import os
import pandas as pd
import pathlib
import torch
from transformers import AutoTokenizer, AutoModel


# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                    'src' /
                    'logging_module' /
                    'log_configuration.yaml')


def encode_text(
        data: pd.DataFrame,
        model_name: str
) -> pd.DataFrame:
    logger.debug('encode_text - Start')

    # Instance the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Instance the transformer
    model = AutoModel.from_pretrained(model_name)

    logger.debug('encode_text - Start')