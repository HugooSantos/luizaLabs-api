from sqlalchemy import TIMESTAMP, Column, Integer, String, Float, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    path_image = Column(String, nullable=False) 
    ean = Column(String(13), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(250), nullable=False)
    sales_location = Column(String(10), nullable=False) 
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)