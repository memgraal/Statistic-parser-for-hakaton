from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class TeamStatistic(Base):
    __tablename__ = "TeamStatistic"  
    
    id = Column(Integer, primary_key=True)
    wins_all = Column(Integer)
    wins_home = Column(Integer)
    wins_guests = Column(Integer)
    wins_in_a_row = Column(Integer)
    
    loses_all = Column(Integer)
    loses_home = Column(Integer)
    loses_guests = Column(Integer)
    loses_in_a_row = Column(Integer)
    
    
engine = create_engine("sqlite:///Statistic.db", echo=True)  
Base.metadata.create_all(engine)  


def get_engine():
    return engine


def get_session():
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


if __name__ == "__main__":
    engine = get_engine()
    session = get_session()
    session.close()
    print("Done")
