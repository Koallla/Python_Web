from aiohttp import web
import aiohttp_jinja2
import asyncio
import jinja2
import threading
from client import *


host = '127.0.0.1'
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template("index.html")
async def handle(request):
    data = await main()
    return {'data': data}


app = web.Application()
app.add_routes(routes)

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))

web.run_app(host=host, app=app)


