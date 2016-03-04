# coding=utf8
from handler.model import User


def get(id):
    return User.get(id).serialize()


def login(username, passwd):
    return User.login(username, passwd).serialize()
