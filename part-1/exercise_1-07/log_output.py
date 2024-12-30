import time, uuid, asyncio, os
from aiohttp import web

message = ""

async def message_generator():
    random_string = str(uuid.uuid4())
    while True:
        global message
        message = time.strftime("%Y-%m-%dT%H:%M:%S") + ": " + random_string
        print(message)
        await asyncio.sleep(5)

async def handle(request):
    return web.Response(text=message)

async def main():
    asyncio.create_task(message_generator())
    
    port = os.environ.get('PORT', 8000)
    
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, None, port)
    await site.start()

    try:
        await asyncio.Future()
    except asyncio.CancelledError:
        pass
    
    await runner.cleanup()

if __name__=="__main__":
    asyncio.run(main())

