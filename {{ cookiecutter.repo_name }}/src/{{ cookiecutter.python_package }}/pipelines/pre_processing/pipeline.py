from kedro.pipeline import Pipeline, node

from .nodes import pre_processing


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                pre_processing,
                inputs="sample_data",
                outputs="samples",
                name="pre_processing",
            )
        ]
    )
