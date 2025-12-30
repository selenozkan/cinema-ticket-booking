# testing basic use of sql with some functions

import sqlite3

def create_table():
    connection = sqlite3.connect("cinema.db") # create a connection object instance
    # create a table
    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL
    );
    """)
    connection.commit()  # commit the changes to db
    connection.close()  # close the connection

def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "90"), ("A2", "1", "100"), ("A3", "0", "80")
    """)
    connection.commit()
    connection.close()

def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor() # reading db records with cursor
    cursor.execute("""
    SELECT * FROM "Seat"
    """)
    results = cursor.fetchall() # cursor contains the data we got, but it's not the final object, so we call the data
    connection.close()
    return results

def select_specific_columns():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM "Seat"
    """)
    results = cursor.fetchall()
    connection.close()
    return results


def select_with_condition():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
     SELECT "seat_id", "price" FROM "Seat" WHERE "price"> 85
     """)
    results = cursor.fetchall()
    connection.close()
    return results

def update_value(occupied, seat_id):
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    UPDATE "Seat" SET "taken"= ? WHERE "seat_id"=?
    """, [occupied, seat_id])
    connection.commit()
    connection.close()

def delete_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    DELETE FROM "Seat" WHERE "seat_id"= "A3"
    """)
    connection.commit()
    connection.close()


#create_table()
#insert_record()
#print(select_all())
#print(select_specific_columns())
#print(select_with_condition())
#delete_record()
update_value(occupied=0, seat_id="A2")