from aiohttp import web
from sqlalchemy.future import select
from app.db import ClimbingGroup, Alpinist, Membership


async def add_alpinist_to_group(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()

        group_name = body['group_name']
        sql_request = select(ClimbingGroup.group_id).filter(ClimbingGroup.group_name == group_name)
        result = session.execute(sql_request)
        group_id = result.scalar_one_or_none()

        if group_id:
            membership = Membership(alpinist_id=body['alpinist_id'],
                                group_id=group_id)
            session.add(membership)
            return web.HTTPOk()
        else:
            return web.HTTPBadRequest()

