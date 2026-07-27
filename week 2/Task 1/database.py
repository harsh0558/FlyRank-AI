from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import db


engine = create_engine(
    url = db.db_url,
    connect_args={"check_same_thread": False}, 
    echo = True
)

sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)

Base.metadata.create_all(bind=engine)

