from sqlalchemy_utils import UUIDType
from datetime import datetime
from repository import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.TEXT)
    writer = db.Column(UUIDType(binary=False), db.ForeignKey("user.id"), nullable=False)
    createdAt = db.Column('createdAt', db.DateTime(timezone=True), default=datetime.utcnow,  nullable=False)
