from aiohttp import web
from app.db import Alpinist


async def add_alpinist(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()
        alpinist = Alpinist(name=body['name'],
                            lastname=body['lastname'])
        session.add(alpinist)
        return web.HTTPOk()





