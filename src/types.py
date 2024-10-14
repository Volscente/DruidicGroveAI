"""
This module includes Pydantic types for the whole project
"""
# Import Standard Modules
from pydantic import BaseModel, validator
from typing import Literal


class BigQueryClientConfig(BaseModel):
    """
    The class implements a Pydantic type for a BigQuery Client
    configuration

    Attributes:
        project_id: String value of the GCP project id
        location: String value of the GCP project location
    """
    project_id: Literal['deep-learning-438509']
    location: Literal['europe-west1']
