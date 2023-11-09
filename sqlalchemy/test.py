from sqlalchemy import create_engine, String, Integer, ForeignKey, CHAR, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Students(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    firstname = Column("First Name", String(50), nullable=False)
    lastname = Column("Last Name", String(50), nullable=False)
    email = Column("E-mail", String, unique=True, nullable=False)
    
    def __init__(self, id, first, last, email):
        self.id = id
        self.firstname = first
        self.lastname = last
        self.email = email
        
    def __repr__(self):
        return f"({self.id} {self.firstname} {self.lastname} {self.email})"
    
    
    engine = create_engine('sqlite:///students.db', echo=True)
    Base.metadata.create_all(bind=engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    
    
        

