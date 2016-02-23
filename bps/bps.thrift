namespace php tutorial

exception SystemException {
	1: i32 code,
	2: string message
}

service Water {
	i16 ping() throws (1:SystemException SysException)
}