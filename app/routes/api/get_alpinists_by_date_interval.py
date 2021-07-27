from aiohttp.web_response import Response
from sqlalchemy.future import select
from app.db import Alpinist, ClimbingGroup, Climbing, Membership
from app.check_rights import check_read_rights


@check_read_rights
async def get_alpinists_by_date_interval(request):
    with request.app['sessionmaker'].begin() as session:
        body = await request.json()

        start_date = body['start_date']
        end_date = body['end_date']

        sql_request = select(Alpinist.name, Alpinist.lastname).join(Membership).join(ClimbingGroup).join(Climbing).where(start_date > Climbing.start_date).where(end_date < Climbing.end_date)
        result = session.execute(sql_request).all()

        return Response(text=str(result))
