from aiohttp.web_response import Response
from sqlalchemy.future import select
from sqlalchemy import func
from app.db import Alpinist, ClimbingGroup, Climbing, Membership, Mountain
from app.check_rights import check_read_rights


async def get_alp_count_by_mountain(request):
    with request.app['sessionmaker'].begin() as session:

        # mount_name = body['mount_name']

        sql_request = select(func.count(Alpinist.alpinist_id)).join(Membership).join(ClimbingGroup).join(Climbing).join(Mountain).group_by(Mountain.name)
        result = session.execute(sql_request).all()

        return Response(text=str(result))
