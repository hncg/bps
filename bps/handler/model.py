# coding=utf8
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from handler import DBSession

from cg_core.utils import serialize_to
from thrift_files.bps import ttypes

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
    user_id = Column(Integer, index=True)
    content = Column(Text)
    time = Column(DateTime)
    author = Column(String(32))
    title = Column(String(128))

    @classmethod
    def mget(cls, query):
        return session.query(cls).offset(query.offset).limit(query.limit).all()

    @classmethod
    def add(cls, **kwds):
        session = DBSession()
        session.add(cls(**kwds))
        session_commit()
        try:
            session.flush()
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise(SQLAlchemyError)
        finally:
            session.close()
        return

    def serialize(self):
        return serialize_to(self, ttypes.Article)


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
        return session.query(cls).all()

    @classmethod
    def mget_by_parent_ids(cls, parent_ids=[]):
        return session.query(cls).filter(cls.parent_id.in_(parent_ids)).all() # noqa

    @classmethod
    def add(cls, **kwds):
        session = DBSession()
        session.add(cls(**kwds))
        session_commit()
        try:
            session.flush()
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise(SQLAlchemyError)
        finally:
            session.close()
        return

    def serialize(self):
        return serialize_to(self, ttypes.Comment)


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    sid = Column(String(256))
    username = Column(String(64))
    password = Column(String(256))
    niker = Column(String(32))
    phone = Column(String(32))
    last_ip = Column(String(64))
    last_time = Column(DateTime)
    is_lock = Column(Integer)
    device = Column(String(128))

    @classmethod
    def get(cls, id):
        result = session.query(cls).filter(cls.id == id).first()
        if not result:
            raise(ttypes.UserException(
                code=1,
                message='空'
            ))
        return result

    @classmethod
    def login(cls, username, passwd):
        result = session.query(cls).filter(cls.username == username and
                                           cls.password == passwd).first()
        if not result:
            raise(ttypes.UserException(
                code=1,
                message='空'
            ))
        return result

    def serialize(self):
        return serialize_to(self, ttypes.User)
