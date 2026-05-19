from sqlalchemy import create_engine,text

class DBConnection:

    DB_URL= 'mysql+pymysql://root:M1racle%20123@localhost/ITG_170'
    engine = create_engine(DB_URL)

    with engine.connect() as connection:
        query = text("INSERT INTO users (name, age) VALUES (:name, :age)")

        connection.execute(query, {"name": "Rahul", "age": 25})

        connection.commit()
