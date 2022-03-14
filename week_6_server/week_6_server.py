import asyncio
from collections import defaultdict


class KeyValueStorage(defaultdict):

    def __init__(self, *_args):
        super().__init__(dict)

    def get(self, key):
        if key in self:
            return ''.join([f"{key} {value} {timestamp}\n"
                            for timestamp, value in self[key].items()])
        else:
            return ''

    def get_all(self):
        return ''.join([f"{key} {value} {timestamp}\n"
                        for key in self
                        for timestamp, value in self[key].items()])

    def put(self, key, value, timestamp):
        self[key][timestamp] = value


class ClientServerProtocol(asyncio.Protocol):

    storage = KeyValueStorage()

    def connection_made(self, transport):
        self.transport = transport

    @staticmethod
    def _process_data(querry: str):

        def return_wc_error():
            return "error\nwrong command\n\n"

        def return_correct(data=""):
            return f"ok\n{data}\n"

        def put_data(key, value, timestamp):

            try:
                value = float(value)
                timestamp = int(timestamp)
            except ValueError:
                return return_wc_error()

            ClientServerProtocol.storage.put(
                key, value, timestamp
            )
            return return_correct()

        def get_data(key):
            return return_correct(ClientServerProtocol.storage.get(key))

        def get_all():
            return return_correct(ClientServerProtocol.storage.get_all())

        tplq = querry.strip().split()
        if len(tplq) == 4 and tplq[0] == "put" and tplq[1] != "*":
            return put_data(*tplq[1:])
        elif len(tplq) == 2 and tplq[0] == "get":
            if tplq[1] == "*":
                return get_all()
            else:
                return get_data(tplq[1])
        else:
            return return_wc_error()

    def data_received(self, data):
        # print('accepted>>', data.decode())
        resp = ClientServerProtocol._process_data(data.decode())
        # print('sent>>', resp)
        self.transport.write(resp.encode())


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    pair = ('127.0.0.1', 10001)
    run_server(*pair)
