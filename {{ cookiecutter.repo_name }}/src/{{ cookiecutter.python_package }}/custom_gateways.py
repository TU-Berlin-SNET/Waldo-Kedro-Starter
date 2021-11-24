"""
Custom gateway implementations
"""

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

import logging
from typing import Dict, Any

from kedro.pipeline.node import Node
from pandas import DataFrame

import waldo_kedro_plugin.gateway as gateway


class DataFrameValidatorGateway(gateway.WaldoGateway):
    """Gateway implementation that checks if any of the input/output parameters is a dataframe"""
    def validate_input(self, node: Node, inputs: Dict[str, Any]):
        """
        validate the input data
        :param:
            node: A kedro node
            inputs: Pandas Dataframe
        :return:
            True: If Dataframe exists in node

        """

        for i in inputs.values():
            if isinstance(i, DataFrame):
                logging.info(f"DataFrame found in node {node.name}")
                return True

        logging.error(f"There was no DataFrame found in node {node.name}")
        exit(-1)

    def validate_output(self, node: Node, outputs: Dict[str, Any]):
        """
        validate the output data
        :param:
            node: A kedro node
            inputs: Pandas Dataframe
        :return:
            True: If Dataframe exists in node
        """

        for i in outputs.values():
            if isinstance(i, DataFrame):
                logging.info(f"DataFrame found in node {node.name}")
                return True

        logging.error(f"There was no DataFrame found in node {node.name}")
        exit(-1)
