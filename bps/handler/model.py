# coding=utf8
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from handler import DBSession

Base = declarative_base()
session = DBSession()


def session_commit():
    try:
        session.flush()
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise(SQLAlchemyError)
    finally:
        session.close()


class Article(Base):

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    time = Column(DateTime)
    author = Column(String(32))
    title = Column(String(128))

    @classmethod
    def mget(cls, offset=0, limit=10):
        return DBSession().query(cls).all()


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer)
    user_id = Column(Integer)
    content = Column(Text)
    time_at = Column(DateTime)
    user_niker = Column(String(32))

    @classmethod
    def mget(cls, offset=0, limit=10):
        return DBSession().query(cls).all()
