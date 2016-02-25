# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://cg:123456@localhost:3306/blog?charset=utf8')
DBSession = sessionmaker(bind=engine)
