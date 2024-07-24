# Program to create a database in SQLite

import time
import sqlite3

db_name = "class_logs.db"  # Name of the database

# This is purely for decoration
def loading(claim):
    if claim == "start":
        statement = "Initializing"
    else:
        statement = "Loading"
    print(statement, end = "")
    for x in range(3):
        print(".", end = "")
        time.sleep(1.2)
    print()

# "wait()" is nicer to look at than "time.sleep()"
# Also, this function saves some lines of code by not having to type in the same thing after every print statement (time.sleep)
def wait(num, message):
    print(message)
    if num == 1:
        time.sleep(3)
    elif num == 2:
        time.sleep(0.1)

def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print(f"Successfully connected to {db_name}")
    return db_conn, db_cursor

def welcome_message():
    wait(1, "Welcome to my database program!")
    loading("start")

def create_table():
    sql = "create table module_eight (id integer, assignment integer, title text, due date, hours real, rating real)"

def drop_table():
    sql = "drop table if exists module_eight"

def insert_record():
    sql = "insert into module_eight values (?, ?, ?, ?, ?, ?)"

def select_all():  # Select without where clause
    sql = "select * from module_eight"

def select_record():  # Select WITH where clause
    sql = "select * from module_eight where id = ?"

def update_record():
    sql = "update module_eight set hours = ?, rating = ? where id = ?"

def delete_record():
    sql = "delete module_eight where id = ?"

def display_menu(db_conn, db_cursor):
    while True:
        wait(2, "\nMenu:")
        wait(2, "Enter S to get started and create a new database")
        wait(2, "Enter C to create a new record")
        wait(2, "Enter R to retrieve data")
        wait(2, "Enter U to update a record")
        wait(2, "Enter D to delete a record")
        wait(2, "Enter Q to quit the program")
        user_input = input("Enter your choice: ").lower()

        if user_input.upper() == "s":
            drop_table(db_conn, db_cursor)
            create_table(db_conn, db_cursor)
        elif user_input.upper() == "c":
            insert_record(db_conn, db_cursor)
        elif user_input.upper() == "r":
            select_all(db_conn, db_cursor)
        elif user_input.upper() == "u":
            update_record(db_conn, db_cursor)
        elif user_input.upper() == "d":
            delete_record(db_conn, db_cursor)
        elif user_input.upper() == "q":
            break
        else:
            print("Invalid choice. Try that again...")

        db_conn.commit()
        select_all()


def close_db(db_conn):
    db_conn.close()
    print(f"\nConnection to {db_name} is now closed. Goodbye :(")

def main():
    db_conn, db_cursor = connect_to_db()
    welcome_message()
    display_menu(db_conn, db_cursor)
    close_db(db_conn)

# if __name__ == "__main__":
#     main()