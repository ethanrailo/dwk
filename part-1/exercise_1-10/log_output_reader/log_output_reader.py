import uuid, asyncio, os
from aiohttp import web

random_string = str(uuid.uuid4())
logfile = os.environ.get('LOGFILE_PATH', "log-output.txt")
port = os.environ.get('PORT', 8000)

def read_log(file):
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
    except:
        return("Timestamp file {} not found".format(logfile))
    else:
        return(content)

async def handle(request):
    return web.Response(text="{}: {}".format(read_log(logfile), random_string))

async def main():  
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

