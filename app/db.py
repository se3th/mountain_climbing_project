from aiohttp import web
from sqlalchemy import create_engine, Column, Date, VARCHAR, INTEGER, ForeignKey, FLOAT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import BIT


Declarative_base = declarative_base()


class Alpinist(Declarative_base):
    __tablename__ = "alpinist"

    alpinist_id = Column('alp_id', INTEGER, primary_key=True, nullable=False)
    name = Column('name', VARCHAR, nullable=False)
    lastname = Column('lastname', VARCHAR, nullable=False)


class Mountain(Declarative_base):
    __tablename__ = 'mountain'

    mountain_id = Column('mountain_id', INTEGER, primary_key=True, nullable=False)
    name = Column('name', VARCHAR, nullable=False)
    height = Column('height', FLOAT, nullable=False)
    country = Column('country', VARCHAR, nullable=False)
    region = Column('region', VARCHAR, nullable=False)
    conquered = Column('conquered', BIT, nullable=False)


class ClimbingGroup(Declarative_base):
    __tablename__ = 'climbing_group'

    group_id = Column('group_id', INTEGER, primary_key=True, nullable=False)
    group_name = Column('group_name', VARCHAR, nullable=False)


class Climbing(Declarative_base):
    __tablename__ = 'climbing'

    climb_id = Column('climb_id', INTEGER, primary_key=True, nullable=False)
    mountain_id = Column('mountain_id', INTEGER, ForeignKey('mountain.mountain_id'), nullable=False)
    group_id = Column('group_id', INTEGER, ForeignKey('climbing_group.group_id'), nullable=False)
    start_date = Column('start_date', Date, nullable=False)
    end_date = Column('end_date', Date, nullable=False)


class Membership(Declarative_base):
    __tablename__ = 'membership'

    membership_id = Column('membership_id', INTEGER, primary_key=True, nullable=False)
    group_id = Column('group_id', INTEGER, ForeignKey('climbing_group.group_id'), nullable=False)
    alpinist_id = Column('alp_id', INTEGER, ForeignKey('alpinist.alp_id'), nullable=False)


class User(Declarative_base):
    __tablename__ = 'db_user'

    user_id = Column('user_id', INTEGER, primary_key=True, nullable=False)
    username = Column('username', VARCHAR, nullable=False)
    password = Column('password', VARCHAR, nullable=False)
    user_rights = Column('user_rights', VARCHAR, nullable=True)


async def init_db(app: web.Application) -> None:
    db_url = app["config"]["url"]
    engine = create_engine(db_url,)
    app['sessionmaker'] = sessionmaker(engine)


async def close_db(app: web.Application) -> None:
    app['sessionmaker'].close_all()

