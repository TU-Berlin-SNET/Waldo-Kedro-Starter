"""
ORM for the input data
"""

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
