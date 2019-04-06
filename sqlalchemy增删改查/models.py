# coding: utf-8
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    pwd = Column(String(255), nullable=False)
    reg_time = Column(DateTime)
