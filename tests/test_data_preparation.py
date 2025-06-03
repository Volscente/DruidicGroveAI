"""
This test module includes all the tests for the
module src.data_preparation
"""

# Import Standard Libraries
from typing import List, Tuple
import numpy as np
import pytest

# Import Package Modules
from src.data_preparation.data_preparation import StackOverflowDataPreparation
from src.bigquery_connector.bigquery_connector import BigQueryConnector
from src.data_preparation.data_preparation_utils import (
    generate_embeddings,
    compress_embeddings,
    encode_text,
)
from src.types import EmbeddingsConfig, CompressEmbeddingsConfig, EncodingTextConfig


@pytest.mark.skip(
    reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
@pytest.mark.parametrize(
    "input_tables, dataset_name",
    [
        (
            ["test_users_information", "test_top_rarest_badges", "test_post_answers"],
            "dim_stackoverflow_data_model",
        )
    ],
)
def test_load_input_tables(
    fixture_stackoverflow_data_preparation: StackOverflowDataPreparation,
    fixture_bigquery_connector: BigQueryConnector,
    input_tables: List[str],
    dataset_name: str,
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation.StackOverflowDataPreparation._load_input_tables
    by ensuring the input tables exist on BigQuery

    Args:
        fixture_stackoverflow_data_preparation (StackOverflowDataPreparation): Object for data preparation
        fixture_bigquery_connector (BigQueryConnector): Object for BigQuery connector to check if input tables exist
        input_tables (List[str]): List of input tables to check
        dataset_name (str): Name of the dataset to use
    """
    # Load input tables
    fixture_stackoverflow_data_preparation._load_input_tables()

    assert fixture_bigquery_connector.table_exists(input_tables[0], dataset_name)
    assert fixture_bigquery_connector.table_exists(input_tables[1], dataset_name)
    assert fixture_bigquery_connector.table_exists(input_tables[2], dataset_name)


@pytest.mark.skip(
    reason="This test is skipped because GCP credentials are not stored on GitHub Secret"
)
@pytest.mark.parametrize(
    "dataset_name, table_name, expected_rows",
    [("dim_stackoverflow_data_model", "test_raw_dataset", 2)],
)
def test_load_raw_dataset(
    fixture_stackoverflow_data_preparation: StackOverflowDataPreparation,
    fixture_bigquery_connector: BigQueryConnector,
    dataset_name: str,
    table_name: str,
    expected_rows: int,
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation.StackOverflowDataPreparation._load_raw_dataset
    by count the number of rows in the created table

    Args:
        fixture_stackoverflow_data_preparation (StackOverflowDataPreparation): Data preparation object
        fixture_bigquery_connector (BigQueryConnector): BigQuery connector object for querying the table
        dataset_name (String): Dataset name to use
        table_name (String): Table name to use
        expected_rows (Integer): Expected number of rows in the table
    """
    # Load the raw dataset
    fixture_stackoverflow_data_preparation._load_raw_dataset()

    # Retrieve project id
    project_id = fixture_bigquery_connector._client_config.project_id

    # Retrieve number of rows
    rows_number = (
        fixture_bigquery_connector._client.query(
            f"SELECT COUNT(*) FROM `{project_id}.{dataset_name}.{table_name}`"
        )
        .result()
        .to_dataframe()
        .iloc[0, 0]
    )

    assert rows_number == expected_rows


@pytest.mark.parametrize(
    "text, expected_shape",
    [
        (["This is a sample test. Please encode it, oh great Omnissiah"], (1, 384)),
        (["text 1", "text 2"], (2, 384)),
    ],
)
def test_generate_embeddings(
    text: List[str], expected_shape: Tuple[int, int], fixture_embeddings_config: EmbeddingsConfig
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation_utils.generate_embeddings

    Args:
        text (List[str]): Input text
        expected_shape (Tuple[int, int]): Expected shape of the output
        fixture_embeddings_config (EmbeddingsConfig): Object including embedding configurations
    """
    # Generate embeddings
    embeddings = generate_embeddings(text, fixture_embeddings_config)

    assert embeddings.shape == expected_shape


@pytest.mark.parametrize(
    "input_embeddings, expected_shape", [(np.random.random((20, 16)), (20, 4))]
)
def test_compress_embeddings(
    input_embeddings: np.ndarray,
    expected_shape: Tuple[int, int],
    fixture_compress_embeddings_config: CompressEmbeddingsConfig,
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation_utils.compress_embeddings

    Args:
        input_embeddings (numpy.ndarray): Input embeddings
        expected_shape (Tuple[int, int]): Expected compressed embeddings' shape
        fixture_compress_embeddings_config (CompressEmbeddingsConfig): Object compressing embedding configurations
    """
    # Compress embeddings
    compressed_embeddings = compress_embeddings(
        input_embeddings, fixture_compress_embeddings_config
    )

    assert compressed_embeddings.shape == expected_shape


def test_encode_text(
    fixture_sentences: List[str], fixture_encode_text_config: EncodingTextConfig
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation_utils.encode_text
    by passing an input text, encoding it and checking if the encoded text is correct.

    Args:
        fixture_sentences (List[str]): Input text sentences
        fixture_encode_text_config (EncodingTextConfig): Object including text encoding configurations
    """
    # Encode the text
    encoded_texts = encode_text(fixture_sentences, fixture_encode_text_config)

    assert encoded_texts.shape == (400, 4)
