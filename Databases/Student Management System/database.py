from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,insert,select,update,delete,Computed

engine = create_engine(r"sqlite:///C:\Users\pc\Documents\Python Developer Roadmap\Databases\Student Management System\student_database.db",echo=True)
metadata = MetaData()

students_table = Table(
        "students",
          metadata,
        Column("id", Integer, primary_key=True, autoincrement=True), 
        Column("name", String(255), nullable=False),
        Column("age", Integer, nullable=False),
        Column("department", String(255), nullable=False),
        Column("email", String(255), nullable=False),
        Column("matric_no", String(100), Computed("department ||'/' || id"))                       )
    

def add_student(name:str,age:int,department:str,email:str):
    with engine.connect() as database_connection:
        insert_statement = insert(students_table).values(name=name, age=age,department=department,email=email)   
        database_connection.execute(insert_statement)
        database_connection.commit()

def view_students():
    with engine.connect() as database_connection:
        view_statement = select(students_table.c)
        table = database_connection.execute(view_statement)
        for row in table:
            print(row)

def search_student(matric_no):
    """Search for a student in the database, the search parameter is the column name and the search_item is 
    who is to be found"""
    with engine.connect() as database_connection:
        search_statement = select(students_table).where(students_table.c.matric_no == matric_no)
        students = database_connection.execute(search_statement)
        for student in students:
            print(student)

def update_student(matric_no,name = None,age = None,department = None,email = None):
    """Update data """
    search = {"name": name, "age": age, "email": email, "department": department}
    valid_searches = {key: value for key, value in search.items() if value is not None}
    with engine.connect() as database_connection:
        update_statement = update(students_table).where(students_table.c.matric_no == matric_no).values(**valid_searches)
        database_connection.execute(update_statement)
        database_connection.commit()

def delete_student(matric_no):
    delete_statement=delete(students_table).where(students_table.c.matric_no == matric_no)
    with engine.connect() as database_connection:
        database_connection.execute(delete_statement)
        database_connection.commit()


metadata.create_all(engine)
search_student("cpe/11")
view_students()