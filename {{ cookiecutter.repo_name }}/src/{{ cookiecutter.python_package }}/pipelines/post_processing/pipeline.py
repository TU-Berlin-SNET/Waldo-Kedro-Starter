from kedro.pipeline import Pipeline, node
from .nodes import os_variance, os_median


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(os_variance, inputs="outliers", outputs=None, name="variance"),
            node(os_median, inputs="outliers", outputs=None, name="median"),
        ]
    )
