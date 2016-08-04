# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../')
import env  # noqa
db_info = 'mysql://' + env.db_user + ':' + env.db_passwd + '@' + env.db_host + ':' + env.db_port + '/' + env.db_name+'?charset=utf8&unix_socket=' + env.socket  # noqa
engine = create_engine(db_info, echo=env.db_debug, pool_size=env.db_pool_size)
DBSession = sessionmaker(bind=engine)
