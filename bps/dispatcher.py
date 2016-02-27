# coding=utf8
from handler import (
    article,
    comment,
)


class Dispatcher(object):

    def ping(self):
        print "ping is ok"
        return 1

    def mget_blog(self):
        return article.mget()

    def mget_comment(self):
        return comment.mget()

    def get_comment_map_by_parent_ids(self, parent_ids=[]):
        return comment.mget_map_by_parent_ids(parent_ids)
