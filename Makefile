thrift_dir:
	cd bps &&\
	mkdir -p thrift_files

build:thrift_dir
	cd bps &&\
	thrift --gen py -out thrift_files bps.thrift

install:
	mkdir -p  ~/.pip && cp pip.conf ~/.pip/ && pip install --trusted-host pypi.douban.com -r requirements.txt

start:
	cd bps &&\
	python start_server.py

ping:
	cd bps && \
	python client.py
