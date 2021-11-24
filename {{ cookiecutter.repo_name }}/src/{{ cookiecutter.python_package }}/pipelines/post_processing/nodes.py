"""
Post-processing nodes
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
