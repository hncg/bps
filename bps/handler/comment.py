# coding=utf8
from handler.model import Comment
from cg_core import utils


def mget():
    return [comment.serialize() for comment in Comment.mget()]


def mget_map_by_parent_ids(ids=[]):
    comments_list = {}
    """ or like this
    return [{comments_list[_.parent_id]: comments_list[_.parent_id].append(_)
            and comments_list[_.parent_id] if comments_list.get(_.parent_id)
            else [_]} for _ in Comment.mget_by_parent_ids(ids)]

    """
    for comment in Comment.mget_by_parent_ids(ids):
        if comments_list.get(comment.parent_id):
            comments_list[comment.parent_id].append(comment.serialize())
        else:
            comments_list[comment.parent_id] = [comment.serialize()]
    return comments_list


def add(comment_arg):
    return Comment.add(
        user_id=comment_arg.user_id,
        parent_id=comment_arg.parent_id,
        content=comment_arg.content,
        time_at=utils.utc2datetime(comment_arg.time_at),
        user_niker=comment_arg.user_niker,
    )
