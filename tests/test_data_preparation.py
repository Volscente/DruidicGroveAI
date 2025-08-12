"""
This test module includes all the tests for the
module src.data_preparation
"""

# Import Standard Libraries
from typing import List, Tuple
import pandas as pd
import numpy as np
import pytest

# Import Package Modules
from src.data_preparation.data_preparation import StackOverflowDataPreparation
from src.bigquery_connector.bigquery_connector import BigQueryConnector
from src.data_preparation.data_preparation_utils import (
    generate_embeddings,
    compress_embeddings,
    encode_text,
    extract_date_information,
    standardise_features,
    drop_outliers,
    manage_nan_values,
    prepare_numerical_features,
    create_flag_feature,
)
from src.custom_types import (
    EmbeddingsConfig,
    CompressEmbeddingsConfig,
    EncodingTextConfig,
    DateExtractionConfig,
    NumericalFeaturesConfig,
    FlagFeatureConfig,
)


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


@pytest.mark.parametrize(
    "input_data, expected_columns",
    [
        (
            pd.DataFrame({"creation_date": ["01/01/2020", "01/01/2021", "01/01/2022"]}),
            ["creation_date", "creation_date_year", "creation_date_month"],
        )
    ],
)
def test_extract_date_information(
    fixture_date_extraction_config: DateExtractionConfig,
    input_data: pd.DataFrame,
    expected_columns: List[str],
) -> bool:
    """
    Test the function
    src/data_preparation/data_preparation_utils.extract_date_information

    Args:
        fixture_date_extraction_config (DateExtractionConfig): Object including date extraction config
        input_data (pd.DataFrame): Input data
        expected_columns (List[str]): Expected columns
    """
    # Extract date information
    output_data = extract_date_information(input_data, fixture_date_extraction_config)

    assert output_data.columns.to_list() == expected_columns


@pytest.mark.parametrize(
    "input_data, expected_values",
    [(pd.DataFrame({"reputation": [12.5, 15.8, 19.7, 50.2]}), [0.0, 0.08, 0.19, 1.0])],
)
def test_standardise_features(
    fixture_numerical_features_config: NumericalFeaturesConfig,
    input_data: pd.DataFrame,
    expected_values: List[float],
) -> bool:
    """
    Test the function src/data_preparation/data_preparation_utils.standardise_features.

    Args:
        fixture_numerical_features_config (NumericalFeaturesConfig): Object including numerical feature transformation configurations
        input_data (pd.DataFrame): Input data
        expected_values (List[float]): Expected standardised values
    """
    # Apply the standardisation
    input_data = standardise_features(input_data, fixture_numerical_features_config)

    # Compute column column
    output_column_name = f"{fixture_numerical_features_config.column_name}_standardised"

    assert input_data.loc[:, output_column_name].to_list() == pytest.approx(
        expected_values, abs=0.1
    )


@pytest.mark.parametrize(
    "input_data, expected_values",
    [(pd.DataFrame({"reputation": [12.5, 15.8, 19.7, 980.2]}), [12.5, 15.8, 19.7])],
)
def test_drop_outliers(
    fixture_numerical_features_config: NumericalFeaturesConfig,
    input_data: pd.DataFrame,
    expected_values: List[float],
) -> bool:
    """
    Test the function src/data_preparation/data_preparation_utils.drop_outliers.

    Args:
        fixture_numerical_features_config (NumericalFeaturesConfig): Object including numerical feature transformation configurations
        input_data (pd.DataFrame): Input data
        expected_values (List[float]): Expected standardised values
    """
    # Apply the drop of outliers
    input_data = drop_outliers(input_data, fixture_numerical_features_config)

    # Compute column column
    output_column_name = f"{fixture_numerical_features_config.column_name}"

    assert input_data.loc[:, output_column_name].to_list() == expected_values


@pytest.mark.parametrize(
    "input_data, expected_output_rows",
    [(pd.DataFrame({"reputation": [12.5, 15.8, 19.7, None], "views": [10, 20, np.nan, 50]}), 3)],
)
def test_manage_nan_values(
    fixture_numerical_features_config: NumericalFeaturesConfig,
    input_data: pd.DataFrame,
    expected_output_rows: int,
) -> bool:
    """
    Test the function src/data_preparation/data_preparation_utils.manage_nan_values.

    Args:
        fixture_numerical_features_config (NumericalFeaturesConfig): Object including numerical feature transformation configurations
        input_data (pd.DataFrame): Input data
        expected_output_rows (int): Expected number of rows in the output data
    """
    # Apply the drop of outliers
    input_data = manage_nan_values(input_data, fixture_numerical_features_config)

    assert input_data.shape[0] == expected_output_rows


@pytest.mark.parametrize(
    "input_data, expected_values",
    [
        (
            pd.DataFrame(
                {"reputation": [12.5, 15.8, 19.7, None, 800.0], "views": [10, 20, np.nan, 50, 600]}
            ),
            [0.0, 0.4, 1.0],
        )
    ],
)
def test_prepare_numerical_features(
    fixture_numerical_features_config: NumericalFeaturesConfig,
    input_data: pd.DataFrame,
    expected_values: List[float],
) -> bool:
    """
    Test the function src/data_preparation/data_preparation_utils.prepare_numerical_features.

    Args:
        fixture_numerical_features_config (NumericalFeaturesConfig): Object including numerical feature transformation configurations
        input_data (pd.DataFrame): Input data
        expected_values (List[float]): Expected transformed column values
    """
    # Apply transformations
    input_data = prepare_numerical_features(input_data, fixture_numerical_features_config)

    # Compute column column
    output_column_name = f"{fixture_numerical_features_config.column_name}_standardised"

    assert input_data.loc[:, output_column_name].to_list() == pytest.approx(
        expected_values, abs=0.1
    )


@pytest.mark.parametrize(
    "input_data, config, expected_values",
    [
        (
            pd.DataFrame({"name": ["James", None, "Anthony"]}),
            FlagFeatureConfig(column_name="name", output_column_name="name_flag"),
            [True, False, True],
        )
    ],
)
def test_create_flag_feature(
    input_data: pd.DataFrame, config: FlagFeatureConfig, expected_values: List[float]
) -> bool:
    """
    Test the function src/data_preparation/data_preparation_utils.create_flag_feature.

    Args:
        input_data (pd.DataFrame): Input data
        config (FlagFeatureConfig): Object including flag feature transformation configurations
        expected_values (List[float]): Expected transformed column values
    """
    # Compute the flag feature
    transformed_data = create_flag_feature(input_data, config)

    assert transformed_data.loc[:, config.output_column_name].to_list() == expected_values
