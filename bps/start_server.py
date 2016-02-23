# coding=utf8
from thrift_files.water import Water
# from thrift_files.ttypes import SystemException
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from dispatcher import Dispatcher


def start(newcls):
    dispatcher = newcls()
    processor = Water.Processor(dispatcher)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print('Starting the server...')
    server.serve()

if __name__ == '__main__':
    start(Dispatcher)
