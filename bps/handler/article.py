# coding=utf8
from handler.model import (
    Article,
    Comment
)
from thrift_files.bps import ttypes
from cg_core.utils import serialize_to


def mget_blog():
    return [serialize_to(article, ttypes.Blog) for article
            in Article.mget()]


def mget_comment():
    return [serialize_to(comment, ttypes.Comment) for comment
            in Comment.mget()]
