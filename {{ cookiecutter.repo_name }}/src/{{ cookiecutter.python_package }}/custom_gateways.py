"""
Custom gateway implementations
"""

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
