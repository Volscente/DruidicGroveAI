"""
This module includes Pydantic types for the whole project
"""

# Import Standard Modules
from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel, Field


class GPCProjects(str, Enum):
    """
    Available GPC Projects
    """

    DEEP_LEARNING = "deep-learning-438509"


class BigQueryClientConfig(BaseModel):
    """
    BigQuery Client configuration

    Attributes:
        project_id (GPCProjects): The Google Cloud project ID, which is
            restricted to 'deep-learning-438509'.
    """

    project_id: GPCProjects = Field(
        default=GPCProjects.DEEP_LEARNING, description="Project ID on Google Cloud Platform"
    )


class BigQueryQueryParameter(BaseModel):
    """
    BigQuery Query parameter object, including all required fields for defining the parameter

    Attributes:
        name (String): Parameter name
        type (String): Parameter type
        value (Union[str, int, float]): The value of the parameter, which
               can be a string, integer, or float.
    """

    name: str = Field(..., description="Parameter name")
    type: str = Field(..., description="Parameter type according to BigQuery Python SDK")
    value: Union[str, int, float, List] = Field(..., description="Parameter value")


class BigQueryQueryConfig(BaseModel):
    """
    BigQuery Query configuration including all elements for executing a query

    Attributes:
        query_path (String): Query file path
        query_parameters (List[BigQueryQueryParameter]): [Optional] List of BigQuery parameters or a single parameter
        local_path (String): [Optional] Local path where to save the data
        table_name (String): [Optional] Table name
    """

    query_path: str = Field(..., description="Query file path")
    query_parameters: Optional[List[BigQueryQueryParameter]] = Field(
        None, description="List of BigQuery parameters"
    )
    local_path: Optional[str] = Field(None, description="Local path where to save the data")
    table_name: Optional[str] = Field(None, description="Table name")

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

    model_name: str = Field("all-MiniLM-L6-v2", description="Model name")
    numpy_tensor: bool = Field(False, description="Output tensor to be a numpy array")


class EmbeddingsConfig(BaseModel):
    """
    Configuration for an embedding generation model

    Attributes:
        method (String): The embedding approach to use (e.g., SentenceTransformer)
        embedding_model_config (Union[SentenceTransformersConfig]): Model configuration
    """

    method: str = Field("SentenceTransformer", description="Embedding approach to use")
    embedding_model_config: Union[SentenceTransformersConfig] = Field(
        ..., description="Model configuration"
    )


class PCAConfig(BaseModel):
    """
    Configuration for a PCA model

    Attributes:
        n_components (Integer): Number of components
    """

    n_components: int = Field(..., description="Number of components")


class CompressEmbeddingsConfig(BaseModel):
    """
    Configuration for compressing embeddings model

    Attributes:
        method (String): The compress approach to use (e.g., PCA)
        compress_model_config (Union[PCAConfig]): Model configuration
    """

    method: str = Field("PCA", description="Compress approach to use")
    compress_model_config: Union[PCAConfig] = Field(..., description="Model configuration")


class EncodingTextConfig(BaseModel):
    """
    Configuration to encode Text and compress them into a lower
    dimensional vector

    Attributes:
        embeddings_config (EmbeddingsConfig): Configuration for embedding generation
        compress_embeddings_config (CompressEmbeddingsConfig): Configuration for embedding compression
    """

    embeddings_config: EmbeddingsConfig = Field(
        ..., description="Configuration for embedding generation"
    )
    compress_embeddings_config: CompressEmbeddingsConfig = Field(
        ..., description="Configuration for embedding compression"
    )


class DateExtractionConfig(BaseModel):
    """
    Configuration to extract information from a date field

    Attributes:
        column_name (String): Column name containing the date
        extract_year (Boolean): Flag to indicate to extract the year
        extract_month (Boolean): Flag to indicate to extract the month
    """

    column_name: str = Field(..., description="Column name containing the date")
    extract_year: bool = Field(..., description="Flag to indicate to extract the year")
    extract_month: bool = Field(..., description="Flag to indicate to extract the month")


class StandardisationMethod(str, Enum):
    MIN_MAX = "min_max_scaler"
    STANDARD = "standard_scaler"


class OutlierMethod(str, Enum):
    Z_SCORE = "z_score"
    IQR = "iqr"


class NanStrategy(str, Enum):
    DROP = "drop_nan"
    IMPUTE = "simple_imputer"


class NumericalFeaturesConfig(BaseModel):
    """
    Configuration for numerical features transformation

    Attributes:
        column_name (String): Name of the numerical column to process
        standardisation (Optional[StandardisationMethod]): Standardisation method to apply
        drop_outliers (Optional[OutlierMethod]): Outlier removal method to use
        nan_values (Optional[NanStrategy]): Strategy to handle missing values
    """

    column_name: str = Field(..., description="Name of the numerical column to process")
    standardisation: Optional[StandardisationMethod] = Field(
        None, description="Standardisation method to apply"
    )
    drop_outliers: Optional[OutlierMethod] = Field(
        None, description="Outlier removal method to use"
    )
    nan_values: Optional[NanStrategy] = Field(None, description="Strategy to handle missing values")
