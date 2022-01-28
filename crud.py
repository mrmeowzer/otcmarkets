from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from contextlib import contextmanager

engine = create_engine(DATABASE_URI, pool_size=20,
                       max_overflow=20, pool_timeout=180, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine, checkfirst=True)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
