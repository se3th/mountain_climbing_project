from aiohttp import web
from collections import namedtuple
import time
from app.routes.api.add_alpinist import add_alpinist
from app.routes.api.add_mountain import add_mountain
from app.routes.api.change_mountain import change_mountain
from app.routes.api.add_climbing_group import add_climbing_group
from app.routes.api.add_alpinist_to_group import add_alpinist_to_group
from app.routes.api.get_groups_by_mountan import get_groups_by_mountain
from app.routes.api.get_alpinists_by_date_interval import get_alpinists_by_date_interval
from app.routes.api.get_alp_count_by_mountain import get_alp_count_by_mountain


async def a(request):
    return web.HTTPOk()


Route = namedtuple("Route", ['url', 'method', 'function'])
routes = [
    Route('/', 'get', a),
    Route('/aa', 'post', add_alpinist),
    Route('/am', 'post', add_mountain),
    Route('/cmh', 'post', change_mountain),
    Route('/acg', 'post', add_climbing_group),
    Route('/aatg', 'post', add_alpinist_to_group),
    Route('/ggbm', 'get', get_groups_by_mountain),
    Route('/gabdi', 'post', get_alpinists_by_date_interval),
    Route('/gacbm', 'get', get_alp_count_by_mountain)
]


def setup_routes(app: web.Application):
    for route in routes:
        app.router.add_route(route.method, route.url, route.function)
