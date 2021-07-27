from aiohttp import web
from app.db import Mountain


async def add_mountain(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()
        mountain = Mountain(name=body['name'],
                            height=body['height'],
                            country=body['country'],
                            region=body['region'],
                            conquered=body['conquered'],)
        session.add(mountain)
        return web.HTTPOk()
