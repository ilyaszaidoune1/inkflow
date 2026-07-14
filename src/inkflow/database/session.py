from sqlalchemy.orm import sessionmaker

from inkflow.database.engine import engine


SessionLocal = sessionmaker(bind=engine)