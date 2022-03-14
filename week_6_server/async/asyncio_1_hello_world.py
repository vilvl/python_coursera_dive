import asyncio


@asyncio.coroutine
def hello_world():
    while 1:
        print("HW!")
        yield from asyncio.sleep(1.0)


async def hello_world_async():
    while 1:
        print("HW!")
        await asyncio.sleep(1.0)

loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world)
loop.run_until_complete(hello_world_async)
loop.close()


def mian():
    pass


if __name__ = '__main__':
    main()
