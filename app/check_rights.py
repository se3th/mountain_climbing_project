from aiohttp import web
from aiohttp.web_request import Request
from sqlalchemy.future import select
from app.db import User


def check_read_rights(handled_function):
    async def wrapper(*args, **kwargs):
        try:
            request = args[0]
            assert isinstance(request, Request)
            body = await request.json()
            user_id = body['user_id']
        except Exception:
            return web.HTTPBadRequest()
        with request.app['sessionmaker'].begin() as session:
            sql_request = select(User.user_rights).filter(User.user_id == user_id)
            rights = session.execute(sql_request).scalar_one_or_none()
        if not rights or (rights != 'read' and rights != 'write'):
            return web.HTTPForbidden()
        return await handled_function(*args, **kwargs)
    return wrapper

