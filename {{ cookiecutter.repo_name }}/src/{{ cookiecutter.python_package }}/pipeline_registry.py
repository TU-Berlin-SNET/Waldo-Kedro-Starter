"""Project pipelines."""
#  Copyright © 2021 Technische Unversität Berlin, Service-centric Networking (SNET) https://snet.tu-berlin.de/
#  Aljoscha Schulte, Christoph Schulthess, Uttam Dhakal, Zohaib Akhtar Khan
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

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

    pre_pipeline = pre.create_pipeline()
    ad_pipeline = ad.create_pipeline()
    post_pipeline = post.create_pipeline()

    # Instantiate all gateways that are used in this project
    DataFrameValidatorGateway("customAdditionalTag")
    LoggingGateway()

    return {
        "pre": pre_pipeline,
        "ad": ad_pipeline,
        "post": post_pipeline,
        "__default__": pre_pipeline + ad_pipeline + post_pipeline,
    }
