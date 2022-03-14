import socket
from collections import defaultdict
from time import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, ip: str, port: int, timeout=None):

        self.pair = (ip, port)
        self.timeout = timeout
        self.sock = socket.create_connection(self.pair, timeout=timeout)

    def put(self, metric: str, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time())
        self.sock.sendall(f"put {metric} {value} {timestamp}\n".encode("utf8"))
        resp = self.sock.recv(1024).decode("utf8")
        if resp != 'ok\n\n':
            raise ClientError('error while put')

    def get(self, request: str) -> dict:
        querry = 'get ' + request + '\n'
        try:
            self.sock.sendall(querry.encode("utf8"))
            resp = self.sock.recv(1024).decode("utf8")
        except Exception:
            raise ClientError('error while put')
        # 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
        resp_parts = resp.split('\n')
        if not resp_parts:
            raise ClientError('empty response')
        if resp_parts[0] != 'ok':
            raise ClientError('Server error')
        res = defaultdict(list)
        for entrie in resp_parts[1:]:
            if entrie:
                cols = entrie.split()
                if not (len(cols) == 3
                        and cols[1].replace('.', '', 1).isdigit()
                        and cols[2].isdigit()):
                    raise ClientError('incorrect response')
                metric, value, timestamp = cols
                res[metric].append((int(timestamp), float(value)))
        for entrie in res:
            res[entrie].sort()
        return res

    def close(self):
        self.sock.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print(args)
        self.close()
