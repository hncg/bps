# coding=utf-8
from sqlalchemy import create_engine
# from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../')
import env  # noqa
db_info = 'mysql://' + env.db_user + ':' + env.db_passwd + '@' + env.db_host + ':' + env.db_port + '/' + env.db_name+'?charset=utf8&unix_socket=' + env.socket  # noqa
engine = create_engine(db_info, echo=env.db_debug, pool_recycle=3600 * 4, pool_size=100) # noqa
DBSession = sessionmaker(bind=engine)
