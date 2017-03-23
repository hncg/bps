# coding=utf8

from thrift_files.bps import Bps
# from thrift_files.bps import ttypes

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

    print client.ping()
    # print client.get_user(1)
    # print client.mget_blog(ttypes.Query(user_id=1, limit=10, offset=1))
    # print client.get_comment_map_by_parent_ids([1, 6])
    # print client.get_user_by_openid('asa')
    # Close!
    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print(('%s' % (tx.message)))
