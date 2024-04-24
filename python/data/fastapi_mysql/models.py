from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class St_info(Base):
    __tablename__ = 'st_info'

    ST_ID = Column(INT, nullable=False, primary_key = True)
    NAME = Column(TEXT, nullable=True)
    DEPT = Column(TEXT, nullable=True)

class St_grade(Base):
    __tablename__ = 'st_grade'
    ST_ID = Column(INT, nullable=False, primary_key = True)
    Linux = Column(TEXT, nullable=True)
    DB = Column(TEXT, nullable=True)

