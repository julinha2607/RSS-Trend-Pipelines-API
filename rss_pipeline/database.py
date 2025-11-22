#Where we define how our data will be stored in the database using sqlalchemy
#We use an ORM (Object Relational Mapping) to map our database tables to Python classes, which allows us to interact with the database using Python objects
#Without it we would have to write SQL queries to interact with the database

#We define the database schema using Python classes, which are then mapped to database tables
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    link = Column(String, unique=True, index=True)
    published_at = Column(DateTime, default=datetime.utcnow)
    source = Column(String)
    content = Column(Text, nullable=True)

class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True)
    count = Column(Integer, default=0)
    date = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
