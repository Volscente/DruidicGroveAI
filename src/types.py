"""
This module includes Pydantic types for the whole project
"""
# Import Standard Modules
from typing import Literal
from pydantic import BaseModel, validator


class BigQueryClientConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Client
    configuration

    Attributes:

    """
    project_id: Literal['deep-learning-438509']
