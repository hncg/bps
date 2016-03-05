namespace php bps

typedef i64 timesteamp

struct Article {
  1: i32 id,
  2: i32 user_id,
  3: string content,
  4: timesteamp time,
  5: string author,
  6: string title
}


struct Comment {
  1: i32 id,
  2: i32 parent_id,
  3: i32 user_id,
  4: string content,
  5: timesteamp time_at,
  7: string user_niker
}


struct Query {
  1: i32 user_id,
  2: i32 limit = 10,
  3: i32 offset = 0
}

struct User {
  1: i32 id,
  2: string sid,
  3: string username,
  4: string password,
  5: string niker,
  6: string phone,
  7: string last_ip,
  8: timesteamp last_time,
  9: i32 is_lock,
  10: string device,
  11: string openid,
  12: string gender
}

exception SystemException {
	1: i32 code,
	2: string message
}

exception UserException {
  1: i32 code,
  2: string message
}

service Bps {
    i16 ping() throws (1:SystemException SysException),

    list <Article> mget_blog(1:Query query) throws (1:SystemException SysException),

    list <Comment> mget_comment() throws (1:SystemException SysException),

    map <i64, list <Comment>> get_comment_map_by_parent_ids(1:list<i32> parent_ids) throws (1:SystemException SysException),

    void add(1:Article article) throws (1:SystemException SysException),

    User get_user(1:i32 user_id) throws (1:SystemException SysException, 2:UserException Userexception),

    User login_user(1:string username, 2:string passwd) throws (1:SystemException SysException, 2:UserException Userexception),

    void add_comment(1:Comment comment) throws (1:SystemException SysException, 2:UserException Userexception),

    User get_user_by_openid(1:string openid) throws (1:SystemException SysException, 2:UserException Userexception),

    i32 register_user(1:User user) throws (1:SystemException SysException, 2:UserException Userexception)
}