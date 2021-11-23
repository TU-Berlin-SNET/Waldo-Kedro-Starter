"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .custom_gateways import DataFrameValidatorGateway
from waldo_kedro_plugin.gateway import LoggingGateway

from .pipelines import pre_processing as pre
from .pipelines import anomaly_detection as ad
from .pipelines import post_processing as post


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """

    nokia_pipeline = pre.create_pipeline()
    ad_pipeline = ad.create_pipeline()
    post_pipeline = post.create_pipeline()

    # Instantiate all gateways that are used in this project
    DataFrameValidatorGateway("customAdditionalTag")
    LoggingGateway()

    return {
        "nk": nokia_pipeline,
        "ad": ad_pipeline,
        "post": post_pipeline,
        "__default__": nokia_pipeline + ad_pipeline + post_pipeline,
    }
