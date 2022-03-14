import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    messege = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'recieved {messege} from {addr}')
    writer.close()


pair = ('127.0.0.1', 10001)
loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, *pair, loop=loop)
serv = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

serv.close()
loop.run_until_complete(serv.wait_closed())
loop.close()


def main():
    pass


if __name__ == '__main__':
    main()
