import asyncio, os
from aiohttp import web

counter = 0
port = os.environ.get('PORT', 8080)

def add_count():
    global counter
    counter += 1

async def handle(request):
    message = "pong {}".format(counter)
    add_count()
    return web.Response(text=message)

async def handle_count(request):
    message = "{}".format(counter)
    return web.Response(text=message)

async def main():      
    app = web.Application()
    app.router.add_get('/pingpong', handle)
    app.router.add_get('/pingpong/count', handle_count)
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

