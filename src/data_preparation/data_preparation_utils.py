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
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore
from typing import List

# Import Package Modules
from src.logging_module.logging_module import get_logger
from src.custom_types import (
    EmbeddingsConfig,
    CompressEmbeddingsConfig,
    EncodingTextConfig,
    DateExtractionConfig,
    NumericalFeaturesConfig,
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
    if config.extract_month:
        data[f"{column_name}_month"] = data[column_name].dt.month

    logger.debug("extract_date_information - End")

    return data


def standardise_features(data: pd.DataFrame, config: NumericalFeaturesConfig) -> pd.DataFrame:
    """
    Apply the specific standardisation method in ``config.standardisation`` on the data column ``config.column_name``

    Args:
        data (pd.DataFrame): Input data
        config (NumericalFeaturesConfig): Object including transformation configurations

    Returns:
        (pd.DataFrame): Output data with additional columns
    """
    logger.debug("standardise_features - Start")

    # Retrieve configurations
    column_name = config.column_name
    standardisation = config.standardisation

    logger.info("standardise_features - Column: %s", column_name)

    # Switch based on the standardisation method
    match standardisation:
        case "min_max_scaler":
            logger.info("standardise_features - MinMaxScaler standardisation approach")

            # Instance the MinMaxScaler
            min_max_scaler = MinMaxScaler()

            # Apply transformation
            data.loc[:, f"{column_name}_standardised"] = min_max_scaler.fit_transform(
                data[[column_name]]
            )

        case _:
            logger.error(
                "standardise_features - Unknown standardisation method: %s", standardisation
            )
            raise ValueError("Invalid standardisation method")

    logger.debug("standardise_features - End")

    return data


def drop_outliers(data: pd.DataFrame, config: NumericalFeaturesConfig) -> pd.DataFrame:
    """
    Apply the specific drop outliers method in ``config.drop_outliers`` on the data column ``config.column_name``

    Args:
        data (pd.DataFrame): Input data
        config (NumericalFeaturesConfig): Object including transformation configurations

    Returns:
        (pd.DataFrame): Output data with additional columns
    """
    logger.debug("drop_outliers - Start")

    # Retrieve configurations
    column_name = config.column_name
    drop_outliers_method = config.drop_outliers.method

    logger.info("drop_outliers - Column: %s", column_name)

    match drop_outliers_method:
        case "z_score":
            logger.info("drop_outliers - Z-score Drop Outliers approach")

            # Compute z-score
            data.loc[:, f"{column_name}_{drop_outliers_method}"] = zscore(data[column_name])

            # Drop outliers
            data = data[
                data[f"{column_name}_{drop_outliers_method}"].abs() <= config.drop_outliers.n_std
            ]

        case "iqr":
            logger.info("drop_outliers - IQR Drop Outliers approach")

            # Compute Q1 and Q3
            q1 = data[column_name].quantile(0.25)
            q3 = data[column_name].quantile(0.75)
            iqr = q3 - q1

            # Define the bounds
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            # Filter outliers
            data = data[(data[column_name] >= lower_bound) & (data[column_name] <= upper_bound)]

        case _:
            logger.error("drop_outliers - Unknown drop outliers method: %s", drop_outliers_method)
            raise ValueError("Invalid drop outliers method")

    return data
