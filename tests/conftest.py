"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import os
import pathlib
from typing import List
import pytest
from dynaconf import Dynaconf

# Import Package Modules
from src.types import (
    BigQueryClientConfig,
    BigQueryQueryConfig,
    BigQueryQueryParameter,
    SentenceTransformersConfig,
    EmbeddingsConfig,
    PCAConfig,
    CompressEmbeddingsConfig,
    EncodingTextConfig
)
from src.general_utils.general_utils import (
    read_file_from_path
)
from src.bigquery_connector.bigquery_connector import BigQueryConnector
from src.data_preparation.data_preparation import StackOverflowDataPreparation

# Read the configuration file
config = Dynaconf(settings_files=[pathlib.Path(__file__).parents[1]
                                  / 'configuration'
                                  / 'stackoverflow_settings.toml'],
                  environments=True,
                  env='pytest')


@pytest.fixture
def fixture_bigquery_client_config(
        project_id: str = config['client']['project_id']
) -> BigQueryClientConfig:
    """
    This fixture returns a BigQueryClientConfig object

    Args:
        project_id (String): GCP project id

    Returns:
        client_config (BigQueryClientConfig): BigQuery object
    """
    # Instance a BigQueryClientConfig object
    client_config = BigQueryClientConfig(project_id=project_id)

    return client_config


@pytest.fixture
def fixture_bigquery_connector(
        fixture_bigquery_client_config: BigQueryClientConfig
) -> BigQueryConnector:
    """
    This fixture returns a BigQueryConnector object

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations of BigQuery client

    Returns:
        bigquery_connector (BigQueryConnector): BigQuery Connector object
    """
    # Instance a BigQueryConnector object
    bigquery_connector = BigQueryConnector(client_config=fixture_bigquery_client_config)

    return bigquery_connector


@pytest.fixture
def fixture_read_query_config(
        query_config: dict = config['read_query_config']
) -> BigQueryQueryConfig:
    """
    Fixture for a BigQueryQueryConfig read query configobject

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """
    # Unpack configs
    query_path, query_parameters = query_config['query_path'], query_config['query_parameters']

    return BigQueryQueryConfig(
        query_path=query_path,
        query_parameters=[BigQueryQueryParameter(**query_parameters[parameter_key]) for parameter_key in query_parameters]
    )


@pytest.fixture
def fixture_create_table_query_config(
        query_config: dict = config['create_table_query_config']
) -> BigQueryQueryConfig:
    """
    Fixture for a BigQueryQueryConfig create table query config object

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """
    # Unpack configs
    query_path, query_parameters = query_config['query_path'], query_config['query_parameters']

    return BigQueryQueryConfig(query_path=query_path,
                               query_parameters=[BigQueryQueryParameter(**query_parameters[query_parameter]) for query_parameter in query_parameters])


@pytest.fixture
def fixture_input_table_configs(
        input_tables_config: dict = config['data_preparation']['input_tables']
) -> List[BigQueryQueryConfig]:
    """
    Fixture for providing the input table configurations required for testing or running
    data preparation pipelines.

    Args:
        input_tables_config (Dictionary): The configuration dictionary containing details of
            input tables required for data preparation.

    Returns:
        config_list (List[BigQueryQueryConfig]): List of BigQueryQueryConfig objects representing the input tables.
    """
    # Initialise the list
    config_list = []

    # Fetch the input table configs
    for table in input_tables_config:

        # Retrieve table config
        table_config = input_tables_config[table]

        # Create the BigQuery config
        bigquery_query_config = BigQueryQueryConfig(**table_config)

        # Add to the list
        config_list.append(bigquery_query_config)

    return config_list



@pytest.fixture
def fixture_raw_dataset_config(
        query_config: dict = config['data_preparation']['raw_dataset']
) -> BigQueryQueryConfig:
    """
    Fixture for a BigQueryQueryConfig object including the Test Raw Dataset configurations
    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as object
    """
    return BigQueryQueryConfig(**query_config)


@pytest.fixture
def fixture_stackoverflow_data_preparation(
        fixture_bigquery_client_config: BigQueryClientConfig,
        fixture_input_table_configs: List[BigQueryQueryConfig],
        fixture_raw_dataset_config: BigQueryQueryConfig,
        dataset_name: str = config['data_preparation']['dataset_name'],
) -> StackOverflowDataPreparation:
    """
    Fixture for a StackOverflowDataPreparation object
    from src/data_preparation/data_preparation.StackOverflowDataPreparation class definition.

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations for a BigQueryConnector object
        fixture_input_table_configs (List[BigQueryQueryConfig]): Input table configurations
        fixture_raw_dataset_config (BigQueryQueryConfig): Configurations for a BigQueryQueryConfig object for raw dataset
        dataset_name (String): Dataset name

    Returns:
        stackoverflow_data_preparation (StackOverflowDataPreparation): Object for data preparation
    """

    # Instance a StackOverflowDataPreparation object
    stackoverflow_data_preparation = StackOverflowDataPreparation(
        dataset_name=dataset_name,
        input_tables_configs=fixture_input_table_configs,
        raw_dataset_config=fixture_raw_dataset_config,
        bigquery_client_config=fixture_bigquery_client_config
    )

    return stackoverflow_data_preparation

@pytest.fixture
def fixture_sentence_transformers_config(
        sentence_transformers_config: dict = config['data_preparation']['sentence_transformers_config']
) -> SentenceTransformersConfig:
    """
    Fixture for a SentenceTransformersConfig object
    from src/types.SentenceTransformersConfig class definition.

    Args:
        sentence_transformers_config (Dictionary): Configurations for a SentenceTransformersConfig object

    Returns:
        (SentenceTransformersConfig): SentenceTransformersConfig object with configurations for embedding generation
    """
    return SentenceTransformersConfig(**sentence_transformers_config)



@pytest.fixture
def fixture_embeddings_config(
        fixture_sentence_transformers_config: SentenceTransformersConfig,
        embeddings_config: dict = config['data_preparation']['embeddings_config']
) -> EmbeddingsConfig:
    """
    Fixture for an EmbeddingsConfig object
    from src/types.EmbeddingsConfig class definition.

    Args:
        fixture_sentence_transformers_config (SentenceTransformersConfig): Configurations for a SentenceTransformersConfig object
        embeddings_config (Dictionary): Configurations for an EmbeddingsConfig object

    Returns:
        (EmbeddingsConfig): EmbeddingsConfig object with configurations for embedding generation
    """
    return EmbeddingsConfig(
        method=embeddings_config['method'],
        embedding_model_config=fixture_sentence_transformers_config
    )


@pytest.fixture
def fixture_pca_config(
        pca_config: dict = config['data_preparation']['pca_config']
) -> PCAConfig:
    """
    Fixture for a PCAConfig object
    from src/types.PCAConfig class definition.

    Args:
        pca_config (Dictionary): PCA configurations

    Returns:
        (PCAConfig): PCAConfig object with configurations for PCA
    """
    return PCAConfig(**pca_config)


@pytest.fixture
def fixture_compress_embeddings_config(
    fixture_pca_config: PCAConfig,
    compress_embeddings_config: dict = config['data_preparation']['compress_embeddings_config']
) -> CompressEmbeddingsConfig:
    """
    Fixture for a CompressEmbeddingsConfig object
    from src/types.CompressEmbeddingsConfig class definition.

    Args:
        fixture_pca_config (PCAConfig): Configurations for a PCAConfig object
        compress_embeddings_config (Dictionary): Configurations for a CompressEmbeddingsConfig object

    Returns:
        (CompressEmbeddingsConfig): CompressEmbeddingsConfig object with configurations for compressing embeddings
    """
    return CompressEmbeddingsConfig(
        method=compress_embeddings_config['method'],
        compress_model_config=fixture_pca_config
    )


@pytest.fixture
def fixture_encode_text_config(
        fixture_embeddings_config: EmbeddingsConfig,
        fixture_compress_embeddings_config: CompressEmbeddingsConfig,
) -> EncodingTextConfig:
    """
    Fixture for an EncodeTextConfig object
    from src/types.EncodingTextConfig class definition.

    Args:
        fixture_embeddings_config (EmbeddingsConfig): Configuration for embedding generation
        fixture_compress_embeddings_config (CompressEmbeddingsConfig): Configuration for embedding compression

    Returns:
        (EncodingTextConfig): EncodeTextConfig object with configurations for encoding text
    """
    return EncodingTextConfig(
        embeddings_config=fixture_embeddings_config,
        compress_embeddings_config=fixture_compress_embeddings_config
    )

@pytest.fixture
def fixture_sentences(
        file_path: str = 'data/test/sentences.txt'
) -> List[str]:
    """
    Fixture for a list of sentences to encode.

    Args:
        file_path (String): Path to the file containing the sentences.

    Returns:
        (List[str]): List of sentences to encode
    """
    # Initialise sentences
    sentences = []

    # Retrieve the root path
    root_path = pathlib.Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH'))

    # Update the file_path with the project root directory
    file_path = root_path / pathlib.Path(file_path)

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file.readline()]

    return sentences
