"""
The module includes Pydantic types for BigQuery Connector.
"""

# Import Standard Modules
from enum import Enum
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
