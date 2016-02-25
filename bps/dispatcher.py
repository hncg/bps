# coding=utf8
from handler import article


class Dispatcher(object):

    def ping(self):
        print "ping is ok"
        return 1

    def mget_blog(self):
        return article.mget_blog()

    def mget_comment(self):
        return article.mget_comment()
