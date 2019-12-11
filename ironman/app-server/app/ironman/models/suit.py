import json
from uuid import UUID
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String

Base = declarative_base()

class Suit(Base):
    __tablename__ = 'suit'
    model = Column(String(256), primary_key=True)
    status = Column(String(256), default=None)
    first_appearance = Column(String(256), default=None)
    image_file = Column(String(256), default=None)
    video_file = Column(String(256), default=None)
    description = Column(String(2000), default=None)

    def to_dict(self):
        return {'model': self.model,
                'status': self.status,
                'first_appearance': self.first_appearance,
                'image_file': self.image_file,
                'video_file': self.video_file,
                'description': self.description}
