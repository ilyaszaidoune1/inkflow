from sqlalchemy import create_engine

from inkflow.core.config import settings


engine = create_engine(settings.database_url)