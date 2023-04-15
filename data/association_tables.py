import sqlalchemy

from .db_session import SqlAlchemyBase

association_table_1 = sqlalchemy.Table(
    'user_to_favourite',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('look', sqlalchemy.Integer, sqlalchemy.ForeignKey('looks.id')))

association_table_2 = sqlalchemy.Table(
    'user_to_clothes',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('clothes', sqlalchemy.Integer, sqlalchemy.ForeignKey('clothes.id')))

association_table_3 = sqlalchemy.Table(
    'look_to_clothes',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('look', sqlalchemy.Integer, sqlalchemy.ForeignKey('looks.id')),
    sqlalchemy.Column('clothes', sqlalchemy.Integer, sqlalchemy.ForeignKey('clothes.id')))