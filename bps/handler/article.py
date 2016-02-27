# coding=utf8
from handler.model import Article


def mget():
    return [article.serialize() for article
            in Article.mget()]
