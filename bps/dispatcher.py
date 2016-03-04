# coding=utf8
from handler import (
    article,
    comment,
    user,
)


class Dispatcher(object):

    def ping(self):
        print "ping is ok"
        return 1

    def mget_blog(self, query):
        return article.mget(query)

    def mget_comment(self):
        return comment.mget()

    def get_comment_map_by_parent_ids(self, parent_ids=[]):
        return comment.mget_map_by_parent_ids(parent_ids)

    def add(self, article_arg):
        return article.add(article_arg)

    def get_user(self, user_id):
        return user.get(user_id)

    def login_user(self, username, passwd):
        return user.login(username, passwd)

    def add_comment(self, comment_arg):
        return comment.add(comment_arg)
