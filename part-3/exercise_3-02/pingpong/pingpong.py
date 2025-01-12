import asyncio, os, psycopg2
from aiohttp import web

counter = 0
port = os.environ.get('PORT', 8080)

def connect_to_postgres():
    try:
        conn = psycopg2.connect(
            host=os.environ["PSQL_HOST"],
            dbname=os.environ["PSQL_DBNAME"],
            user=os.environ["PSQL_USER"],
            password=os.environ["PSQL_PASSWORD"]
        )
        print("Connected to postgres successfully!")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to postgres", error)
        return None
  
def store_count_to_sql(conn):
    global counter
    try:
        cur = conn.cursor()

        cur.execute("SELECT EXISTS(SELECT 1 FROM pingpong_count)")
        row_exists = cur.fetchone()[0]

        if not row_exists:
            cur.execute("INSERT INTO pingpong_count (count) VALUES (%s)", (counter,))
        else:
            cur.execute("UPDATE pingpong_count SET count = %s", (counter,))

        conn.commit()
        cur.close()
        print("Count written succesfully to the table.")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating pingpong_count:", error)


def add_count():
    global counter
    counter += 1
    
    conn = connect_to_postgres()

    if conn:
        store_count_to_sql(conn)
        conn.close()

async def handle(request):
    message = "pong {}".format(counter)
    add_count()
    return web.Response(text=message)

async def handle_count(request):
    message = "{}".format(counter)
    return web.Response(text=message)

async def main():      
    app = web.Application()
    app.router.add_get('/', handle)
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

