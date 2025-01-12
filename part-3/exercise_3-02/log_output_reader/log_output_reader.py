import uuid, asyncio, os, requests
from aiohttp import web

random_string = str(uuid.uuid4())
logfile = os.environ.get('LOGFILE_PATH', "log-output.txt")
pingpong_url = os.environ.get('PINGPONG_URL', "http://pingpong-svc:2347/pingpong/count")
port = os.environ.get('PORT', 8000)

def get_pong_count():
    try:
        response = requests.get(pingpong_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching {pingpong_url}: {e}")
    return "Error occured while fetching pong-count"

def read_log(file):
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
    except:
        return("File {} not found".format(file))
    else:
        return(content)

async def handle(request):
    text = f"""
    file content: {read_log('config/information.txt')}
    env variable: MESSAGE={os.environ.get('MESSAGE', 'Env-variable not found')}
    {read_log(logfile)}: {random_string}
    Ping / Pongs: {get_pong_count()}
    """
    return web.Response(text=text)

async def main():  
    app = web.Application()
    app.router.add_get('/logoutput', handle)
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

