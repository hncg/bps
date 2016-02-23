thrift_dir:
	cd bps&&\
	mkdir thrift_files

install:thrift_dir
	cd bps&&\
	thrift --gen py -out thrift_files bps.thrift

start:
	cd bps&&\
	python start_server.py