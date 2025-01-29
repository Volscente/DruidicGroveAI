"""
This module includes Pydantic types for the whole project
"""
# Import Standard Modules
from typing import Literal
from pydantic import BaseModel


class BigQueryClientConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Client
    configuration

    Attributes:

    """
    project_id: str = Literal['deep-learning-438509']

class BigQueryQueryParameters(BaseModel):
    pass
class BigQueryQueryConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Query
    configuration

    Attributes:

    """
    query_path: str
    query_parameters: BigQueryQueryParameters
    local_path: str