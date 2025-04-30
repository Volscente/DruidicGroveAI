"""
This module includes Pydantic types for the whole project
"""
# Import Standard Modules
from typing import Literal, Optional, Union, List
from pydantic import BaseModel


class BigQueryClientConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Client
    configuration.

    Attributes:
        project_id (String): The Google Cloud project ID, which is
            restricted to 'deep-learning-438509'.
    """
    project_id: str = Literal['deep-learning-438509']


class BigQueryQueryParameter(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Query
    parameter

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
    The class implements a Pydantic type for a BigQuery Query
    configuration

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

class EncodingTextConfig(BaseModel):
    """
    The class implements a Pydantic type for the configuration to
    generate embeddings from a Text and compress them into a lower
    dimensional vector

    Attributes:
        model_name (String): The name of the model to generate embeddings
        return_tensors (String): Output tensor types
        truncation (Boolean): Truncation
        padding (Boolean): Padding
        max_length (Integer): Maximum length of tokens
    """
    model_name: str
    return_tensors: str = Literal['pt']
    truncation: bool = True
    padding: bool = True
    max_length: int = 512
