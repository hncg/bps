# coding=utf8

from thrift_files.bps import Bps

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Bps.Client(protocol)
    # Connect!
    transport.open()

    # print client.ping()
    print client.login_user('admin', '21232f297a57a5a743894a0e4a801fc3')
    print client.get_user(1)
    # Close!
    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print(('%s' % (tx.message)))
