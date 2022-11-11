from sqlalchemy import Column, Integer, String, DateTime
from database import Base 
from sqlalchemy.sql import func


#create db model using sqlalchemy
class Item(Base):
    __tablename__ = 'coins'
    id = Column(Integer, primary_key=True)
    coin_name = Column(String(10))
    coin_add = Column(String(256))
    # stat_code = Column(Integer(3))
    time_created = Column(DateTime(timezone=True), server_default=func.now())


