thrift_dir:
	cd bps &&\
	mkdir -p thrift_files

build:thrift_dir
	cd bps &&\
	thrift --gen py -out thrift_files bps.thrift

install:
	sudo apt-get install libmysqlclient-dev &&\
	sudo pip install MySQL-python
	sudo pip install sqlalchemy

start:
	cd bps &&\
	python start_server.py

ping:
	@cd bps && \
	python client.py
