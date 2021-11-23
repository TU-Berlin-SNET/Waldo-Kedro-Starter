from kedro.pipeline import Pipeline, node

from .nodes import anomaly_detection
from waldo_kedro_plugin.nodes import isolation_forest


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                isolation_forest,
                inputs=["samples", "params:model_param1"],
                outputs="outliers",
                name="isolation_forest"
            ),
            node(
                anomaly_detection,
                inputs=["samples", "params:model_param1"],
                outputs="ad_outliers",
                name="anomaly_detection",
            )
        ]
    )
