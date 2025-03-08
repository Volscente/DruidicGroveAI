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
from src.types import (
    EncodingTextConfig
)

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                    'src' /
                    'logging_module' /
                    'log_configuration.yaml')


def encode_text(
        text: str,
        config: EncodingTextConfig,
) -> pd.DataFrame:
    logger.debug('encode_text - Start')

    logger.info(f'encode_text - Instance Tokenizer and Model from %s', model_name)

    # Instance the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config.model_name)

    # Instance the transformer
    model = AutoModel.from_pretrained(config.model_name)

    logger.info('encode_text - Generate Tokens')

    # Generate tokens
    tokens = Tokenizer(text,
                       return_tensors=config.return_tensors,
                       truncation=config.truncation,
                       padding=config.padding,
                       max_length=config.max_length)

    logger.info('encode_text - Generate Tokens')

    logger.debug('encode_text - Start')