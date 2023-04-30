import socket
import logging
import os

HOST = "proxy"
PROXY_PORT = os.getenv("PROXY_PORT")
MULTICAST_IPV = os.getenv("MULTICAST_IPV")
MULTICAST_PORT = os.getenv("MULTICAST_PORT")
SERVER_PORT = os.getenv("SERVER_PORT")
SIZE = 8192*7
FORMATS = ['native', 'xml', 'json', 'protobuf', 'avro', 'yaml', 'msgpack', 'all']


def start():
    logging.basicConfig(level=logging.DEBUG)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    s.bind((HOST, int(PROXY_PORT)))

    while True:
        req, addr = s.recvfrom(SIZE)
        req_args = req.decode().split()
        logging.debug("%s", req)
        response = bytes()
        if len(req_args) != 2 or req_args[1] not in FORMATS:
            continue
        logging.info(f'Type: {req_args[1]}')
        if req_args[1] == 'all':
            s.sendto(req_args[0].encode(), (MULTICAST_IPV, int(MULTICAST_PORT)))
            for i in range(len(FORMATS)):
                data, _ = s.recvfrom(SIZE)
                response += data
        else:
            s.sendto(req_args[0].encode(),  (req_args[1],int(SERVER_PORT)))
            logging.info(f'Sended to {req_args[1]}:{SERVER_PORT}')
            response, _ = s.recvfrom(SIZE)

        s.sendto(response, addr)


if __name__ == '__main__':
    start()
