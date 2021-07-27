from aiohttp import web
from app.db import Mountain
from sqlalchemy.future import select


async def change_mountain(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()

        mountain_name = body['name']
        sql_request = select(Mountain).filter(Mountain.name == mountain_name)
        result = session.execute(sql_request)
        mountain = result.scalar_one_or_none()
        if mountain:
            if not mountain.conquered:
                height = body.get('height')
                country = body.get('country')
                region = body.get('region')
                mountain.height = height or mountain.height
                mountain.country = country or mountain.country
                mountain.region = region or mountain.region
                return web.HTTPOk()
            else:
                return web.HTTPForbidden()
        else:
            return web.HTTPNotFound()



