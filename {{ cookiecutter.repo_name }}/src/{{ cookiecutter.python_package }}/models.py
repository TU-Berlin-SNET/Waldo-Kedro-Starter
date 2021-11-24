"""
ORM for the input data
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

from sqlalchemy import Column, BIGINT, VARCHAR, TIMESTAMP, INT, FLOAT, BOOLEAN, Index
from waldo_kedro_plugin.models import Base


class Samples(Base):
    """
    The Samples class defines the table schema for the input data that is going to be stored to the database
    The table name must not be modified, and the auto-incremented primary key (id) column must not be removed
    Other columns/Indices can be added, deleted or modified based on the structure of the input data
    """

    # IMPORTANT: Must not be modified, keep it as it is
    __tablename__ = "samples"
    id = Column(BIGINT, nullable=False, primary_key=True, autoincrement=True)

    # Can be modified from here onwards
    col1 = Column(FLOAT)
    col2 = Column(FLOAT)
    col3 = Column(FLOAT)

    # placing an index on col1, col2, col3
    __table_args__ = (Index('idx_samples_col1_col2_col3', "col1", "col2", "col3"), )
