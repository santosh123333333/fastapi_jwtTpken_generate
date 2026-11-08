from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase


DATABASE_URL="sqlite:///./auth.db"




# connection established



engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

#creating a session


sessionalocal=sessionmaker(bind=engine)



# dependency database session function



def get_db():
    db=sessionalocal()
    try:
        yield db
    finally:
        db.close()



class Base(DeclarativeBase):
    pass
