from aiohttp import web
import asyncio
from app.routes.routes import setup_routes
from app.db import init_db, close_db

def create_app (config: dict) -> web.Application:
    app = web.Application()
    app["config"] = config
    setup_routes(app)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app




if __name__ == "__main__":
    SERVER = 'DESKTOP-G917ER8\SQLEXPRESS'
    DATABASE = 'mountain_climbing'
    DRIVER = 'ODBC Driver 17 for SQL Server'
    USERNAME = 'n_chernata'
    PASSWORD = '1234'
    DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
    config = {'url': DATABASE_CONNECTION}
    app = create_app(config)
    ssl_context = None
    web.run_app(app,
                host="localhost",
                port=8080,
                ssl_context=ssl_context)

