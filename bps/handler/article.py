# coding=utf8
from handler.model import Article
from cg_core import utils


def mget(query):
    return [article.serialize() for article
            in Article.mget(query)]


def add(article_arg):
    return Article.add(
        title=article_arg.title,
        content=article_arg.content,
        time=utils.utc2datetime(article_arg.time),
        author=article_arg.author,
        user_id=article_arg.user_id,
    )
