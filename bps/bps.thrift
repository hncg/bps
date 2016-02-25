namespace php bps

typedef i64 timesteamp

struct Blog {
  1: i32 id,
  2: string content,
  3: timesteamp time,
  4: string author,
  5: string title
}


struct Comment {
  1: i32 id,
  2: i32 parent_id,
  3: i32 user_id,
  4: string content,
  5: timesteamp time_at,
  7: string user_niker
}


exception SystemException {
	1: i32 code,
	2: string message
}

service Bps {
    i16 ping() throws (1:SystemException SysException),

    list <Blog> mget_blog() throws (1:SystemException SysException)

    list <Comment> mget_comment() throws (1:SystemException SysException)
}