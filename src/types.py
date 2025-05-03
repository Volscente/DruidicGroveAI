"""
This module includes Pydantic types for the whole project
"""
# Import Standard Modules
from typing import Literal, Optional, Union, List
from pydantic import BaseModel


class BigQueryClientConfig(BaseModel):
    """
    BigQuery Client configuration

    Attributes:
        project_id (String): The Google Cloud project ID, which is
            restricted to 'deep-learning-438509'.
    """
    project_id: str = Literal['deep-learning-438509']


class BigQueryQueryParameter(BaseModel):
    """
    BigQuery Query parameter

    Attributes:
        name (String): Parameter name
        type (String): Parameter type
        value (Union[str, int, float]): The value of the parameter, which
               can be a string, integer, or float.
    """
    name: str
    type: str
    value: Union[str, int, float, List]


class BigQueryQueryConfig(BaseModel):
    """
    BigQuery Query configuration

    Attributes:
        query_path (String): Query file path
        query_parameters (List[BigQueryQueryParameter]): [Optional] List of BigQuery parameters or a single parameter
        local_path (String): [Optional] Local path where to save the data
        table_name (String): [Optional] Table name
    """
    query_path: str
    query_parameters: Optional[List[BigQueryQueryParameter]] = None
    local_path: Optional[str] = None
    table_name: Optional[str] = None

    def count_non_none_attributes(self) -> int:
        """
        Compute the number of non-None attributes

        Returns:
            (Integer): Number of non-None attributes
        """
        return sum(1 for field, value in self.__dict__.items() if value is not None)


class SentenceTransformersConfig(BaseModel):
    """
    Configuration for embedding generation with SentenceTransformers library

    Attributes:
        model_name (String): The name of the model to use
        numpy_tensor (Boolean): Output tensor to be a numpy array
    """
    model_name: str
    numpy_tensor:bool = False


class EmbeddingsConfig(BaseModel):
    """
    Configuration for embedding generation model

    Attributes:
        method (String): The embedding approach to use (e.g., SentenceTransformer)
        embedding_model_config (Union[SentenceTransformersConfig]): Model configuration
    """
    method: str
    embedding_model_config: Union[SentenceTransformersConfig]


class PCAConfig(BaseModel):
    """
    Configuration for a PCA model

    Attributes:
        n_components (Integer): Number of components
    """
    n_components: int


class CompressEmbeddingsConfig(BaseModel):
    """
    Configuration for compressing embeddings model

    Attributes:
        method (String): The compress approach to use (e.g., PCA)
        compress_model_config (Union[PCAConfig]): Model configuration
    """
    method: str
    compress_model_config: Union[PCAConfig]



class EncodingTextConfig(BaseModel):
    """
    Configuration to encode Text and compress them into a lower
    dimensional vector

    Attributes:

    """
    embeddings_config: EmbeddingsConfig
    compress_embeddings_config: CompressEmbeddingsConfig
