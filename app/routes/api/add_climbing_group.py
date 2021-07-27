from aiohttp import web
from sqlalchemy.future import select
from app.db import ClimbingGroup, Mountain, Climbing


async def add_climbing_group(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()

        sql_request = select(ClimbingGroup).filter(ClimbingGroup.group_name == body['group_name'])
        result = session.execute(sql_request)
        group = result.scalar_one_or_none()
        if not group:
            climbing_group = ClimbingGroup(group_name=body['group_name'])
            session.add(climbing_group)

            result = session.execute(sql_request)
            group = result.scalar()

        mountain_name = body['mountain_name']
        sql_request = select(Mountain).filter(Mountain.name == mountain_name)
        result = session.execute(sql_request)
        mountain = result.scalar_one_or_none()
        if mountain:
            climbing = Climbing(group_id=group.group_id,
                                mountain_id=mountain.mountain_id,
                                start_date=body['start_date'],
                                end_date=body['end_date'])
            session.add(climbing)
            return web.HTTPOk()
        else:
            return web.HTTPBadRequest()
