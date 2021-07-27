from aiohttp.web_response import Response
from sqlalchemy.future import select
from app.db import Climbing, Mountain, ClimbingGroup
from app.check_rights import check_read_rights


@check_read_rights
def get_groups_by_mountain(request):
    with request.app['sessionmaker'].begin() as session:

        sql_request = select(Mountain.name, ClimbingGroup.group_name, Climbing.end_date).join(Mountain).join(ClimbingGroup).order_by(Climbing.end_date)
        result = session.execute(sql_request).all()

        return Response(text=str(result))
