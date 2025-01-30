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
        project_id: (String) The Google Cloud project ID, which is
            restricted to 'deep-learning-438509'.
    """
    project_id: str = Literal['deep-learning-438509']


class BigQueryQueryParameter(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Query
    parameter

    Attributes:
        name: (String) Parameter name
        type: (String) Parameter type
        value: (Union[str, int, float]): The value of the parameter, which
               can be a string, integer, or float.
    """
    name: str
    type: str
    value: Union[str, int, float]


class BigQueryQueryConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Query
    configuration

    Attributes:
        query_path: (String) Query file path
        query_parameters: [Optional](List[BigQueryQueryParameter] List of BigQuery parameters
        local_path: (String)
    """
    query_path: str
    query_parameters: Optional[List[BigQueryQueryParameter]] = None
    local_path: str