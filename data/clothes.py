import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Clothes(SqlAlchemyBase):
    __tablename__ = 'clothes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("functionality.id"))
    func = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("type.id"))
    season = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("season.id"))
    image = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)

    functionalities = orm.relationship("Functionality")
    types = orm.relationship("Type")
    seasons = orm.relationship("Season")

    looks = orm.relationship("Looks", back_populates='clothes')