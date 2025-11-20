from sqlalchemy import create_engine,Column,Integer,String,Date,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base
from datetime import date

#engine connects to the database by providing a connection object which then allows interaction with the database database_url = #sqlite:///path/to/your/database.db
engine = create_engine(r"sqlite:///C:\Users\pc\Documents\Python Developer Roadmap\Databases\Notes app\notes_database.db", 
                       echo=True)

#Creating a declarative base baseclass called my_base
my_Base= declarative_base()



class Note(my_Base):
    __tablename__ = 'Notes'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    content = Column(String)
    saved = Column(Boolean)
    created_at = Column(Date,default = date.today())




my_Base.metadata.create_all(engine)
My_Sessions = sessionmaker(bind=engine)
my_session = My_Sessions()











































































































