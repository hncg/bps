# coding=utf8
from handler.model import User
from cg_core.utils import utc2datetime


def get(id):
    return User.get(id).serialize()


def login(username, passwd):
    return User.login(username, passwd).serialize()


def get_by_openid(openid):
    return User.get_by_openid(openid).serialize()


def register(user_arg):
    return User.register(
        openid=user_arg.openid,
        sid=user_arg.sid,
        niker=user_arg.niker,
        last_ip=user_arg.last_ip,
        last_time=utc2datetime(user_arg.last_time),
        device=user_arg.device,
        gender=user_arg.gender,
    )
