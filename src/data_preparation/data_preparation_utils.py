"""
The module includes functions for implementing data transformations
"""

# Import Standard Libraries
import os
import numpy as np
import pandas as pd
import pathlib
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from typing import List

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.types import (
    EmbeddingsConfig,
    CompressEmbeddingsConfig,
    EncodingTextConfig,
    DateExtractionConfig,
)

# Setup logger
logger = get_logger(
    os.path.basename(__file__).split(".")[0],
    pathlib.Path(os.getenv("DRUIDIC_GROVE_AI_ROOT_PATH"))
    / "src"
    / "logging_module"
    / "log_configuration.yaml",
)


def generate_embeddings(texts: List[str], embeddings_config: EmbeddingsConfig) -> np.ndarray:
    """
    Generate the embeddings from the input texts through the method
    specified in embeddings_config.method.

    Args:
        texts (String): Input text
        embeddings_config (EmbeddingsConfig): Object including embedding configurations

    Returns:
        sentence_embeddings (numpy.ndarray): Embedded texts (n_samples, embeddings_size)
    """
    logger.debug("generate_embeddings - Start")

    # Retrieve embeddings' method
    method = embeddings_config.method

    # Switch based on the embeddings' method
    match method:
        case "SentenceTransformer":
            logger.info("generate_embeddings - SentenceTransformer embedding approach")

            # Instance model
            model = SentenceTransformer(embeddings_config.embedding_model_config.model_name)

            # generate embeddings
            sentence_embeddings = model.encode(
                texts, convert_to_numpy=embeddings_config.embedding_model_config.numpy_tensor
            )
        case _:
            logger.error("generate_embeddings - Unknown embedding method: %s", method)
            raise ValueError("Invalid embedding method")

    logger.debug("generate_embeddings - End")

    return sentence_embeddings


def compress_embeddings(
    input_embeddings: np.ndarray, compress_embeddings_config: CompressEmbeddingsConfig
) -> np.ndarray:
    """
    Compress the input embeddings with the corresponding selected method in
    `compress_embeddings_config.method`.

    Args:
        input_embeddings (numpy.ndarray): Input embeddings (n_samples, embeddings_size)
        compress_embeddings_config (CompressEmbeddingsConfig): Compress algorithm configs

    Returns:
        compressed_embeddings (numpy.ndarray): Output embeddings compressed (n_samples, n_components)
    """
    logger.debug("compress_embeddings - Start")

    # Retrieve compress method
    method = compress_embeddings_config.method

    # Switch based on the compress method
    match method:
        case "PCA":
            logger.info("compress_embeddings - PCA compress approach")

            # Instance model
            model = PCA(n_components=compress_embeddings_config.compress_model_config.n_components)

            # Compress embeddings
            compressed_embeddings = model.fit_transform(input_embeddings)

        case _:
            logger.error("compress_embeddings - Unknown compression method: %s", method)
            raise ValueError("Invalid compression method")

    logger.debug("compress_embeddings - End")

    return compressed_embeddings


def encode_text(
    texts: List[str],
    config: EncodingTextConfig,
) -> np.ndarray:
    """
    Encode an input text through embeddings and compress their dimensionality.

    Args:
        texts (List[str]): Input texts
        config (EncodingTextConfig): Object including embedding configurations

    Returns:
        compressed_embeddings (numpy.ndarray): Output embeddings compressed (n_samples, n_components)
    """
    logger.debug("encode_text - Start")

    # Generate embeddings
    embeddings = generate_embeddings(texts, config.embeddings_config)

    # Compress embeddings
    compressed_embeddings = compress_embeddings(embeddings, config.compress_embeddings_config)

    logger.debug("encode_text - End")

    return compressed_embeddings


def extract_date_information(data: pd.DataFrame, config: DateExtractionConfig) -> pd.DataFrame:
    """
    Extract date information from a column included in the ``config.column_name`` like the year, the month, etc.

    Args:
        data (pd.DataFrame): Input data
        config (DateExtractionConfig): Configuration including the column_name and date information to extract

    Returns:
        (pd.DataFrame): Output data with additional columns
    """
    logger.debug("extract_date_information - Start")

    # Retrieve column name
    column_name = config.column_name

    # Convert column to datetime
    data[column_name] = pd.to_datetime(data[column_name])

    # Extract date information
    if config.extract_year:
        data[f"{column_name}_year"] = data[column_name].dt.year
    elif config.extract_month:
        data[f"{column_name}_month"] = data[column_name].dt.month

    logger.debug("extract_date_information - End")

    return data
