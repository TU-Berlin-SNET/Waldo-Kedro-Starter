"""
Post-processing nodes
"""

import logging
import pandas as pd
import numpy as np


def os_variance(os: pd.DataFrame):
    """
    Node to calculate the variance of outliers
    :param os: DataFrame with outlier scores
    """

    outliers = os["score"].values
    logging.info(
        f"""\n
                    **************************************************************
                        The variance of outlier scores is {np.var(outliers)}
                    **************************************************************\n"""
    )


def os_median(os: pd.DataFrame):
    """
    Node to calculate the median of outliers
    :param os: DataFrame with outlier scores
    """

    outliers = os["score"].values
    logging.info(
        f"""\n
                    ************************************************************************************************************
                        The median value of outlier scores is {np.median(outliers)}, whereas the mean is {np.mean(outliers)}
                    ************************************************************************************************************\n"""
    )
