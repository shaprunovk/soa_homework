import socket
import logging
import os
import timeit
import struct

from test_data import TEST_DATA
from protocol_serializers.base_serializer import BaseSerializer
from protocol_serializers.avro.avro import AvroSerializer
from protocol_serializers.json.json import JsonSerializer
from protocol_serializers.protobuf.protobuf import ProtobufSerializer
from protocol_serializers.native.native import NativeSerializer
from protocol_serializers.xml.xml import XmlSerializer
from protocol_serializers.yaml.yaml import YamlSerializer
from protocol_serializers.msgpack.msgpack import MsgPackSerializer


def select_format(ser_format):
    serializer = BaseSerializer()
    if ser_format == "avro":
        serializer = AvroSerializer()
    elif ser_format == "json":
        serializer = JsonSerializer()
    elif ser_format == "msgpack":
        serializer = MsgPackSerializer()
    elif ser_format == "native":
        serializer = NativeSerializer()
    elif ser_format == "protobuf":
        serializer = ProtobufSerializer()
    elif ser_format == "xml":
        serializer = XmlSerializer()
    elif ser_format == "yaml":
        serializer = YamlSerializer()
    return serializer


def response(data, serialization_format):
    serializer = select_format(serialization_format)

    ser_time = timeit.timeit(lambda: serializer.serialize(data), number=100)
    serialized_data = serializer.serialize(data)

    deser_time = timeit.timeit(lambda: serializer.deserialize(serialized_data), number=100)


    ans = f'{serialization_format} - {len(serialized_data)}  - {ser_time*1000}ms - {deser_time*1000}ms'
    logging.info(f'Answer: {ans}')
    return ans


if __name__ == '__main__':
    FORMAT = os.getenv("FORMAT")
    MULTICAST_IPV = os.getenv("MULTICAST_IPV")
    MULTICAST_PORT = os.getenv("MULTICAST_PORT")
    SERVER_PORT = os.getenv("SERVER_PORT")

    logging.info(f"Get {FORMAT} format type request")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    server_socket.bind((FORMAT, int(SERVER_PORT)))
    mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_IPV), socket.INADDR_ANY)
    server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    logging.info('Socket configured')

    while True:
        _, addr = server_socket.recvfrom(8192*7)
        logging.debug(TEST_DATA)
        ans = response(TEST_DATA, FORMAT)
        logging.info('Response getted')
        server_socket.sendto(ans.encode(), addr)
        logging.info('Response sended')
