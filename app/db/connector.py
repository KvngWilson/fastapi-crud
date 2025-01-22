from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class PostgresConnector:
  def __init__(self, env: str):
    self.engine = create_engine(f"postgresql://user:password@localhost:5432/{env}")
    self.Session = sessionmaker(bind=self.engine)
    
  def get_session(self):
    return self.Session()