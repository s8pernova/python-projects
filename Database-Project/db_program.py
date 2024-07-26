# Program to create a database using SQLite

import time
import random
import sqlite3

db_name = "class_logs.db"  # Name of the database
table_name = "modules"  # Because there is only one table in this db, I can use it as a variable. And if I ever wanted to change it, I could do it here

# This is purely for decoration
def loading(claim = None):  # The default parameter will be nothing, so if I don't have any arguments, it'll just say "Loading" instead of "Initializing"
    if claim == "start":
        statement = "Initializing"
    else:
        statement = "Loading"
    print(statement, end = "")
    for x in range(random.randint(3, 5)):  # Print a random number of dots in the loading message
        print(".", end = "")
        time.sleep(1.2)
    print()

# This function saves some lines of code by not having to type in time.sleep after every print statement
# Also it's entirely decorational
def wait(num, message = None):
    # If there's no message given, then it'll skip that part and just use this function as another form for time.sleep()
    if message != None:
        print(message)

    if num == 1:
        time.sleep(3)
    elif num == 2:
        time.sleep(0.1)
    elif num == 3:
        time.sleep(2)

# Function to ask the user for confirmation
def confirm_action(message) -> bool:  # Added an annotation because I'm still learning about those and I wanted to try it out
    while True:
        user_choice = input(message).lower()
        if user_choice == 'y':
            return True
        elif user_choice == 'n':
            return False
        else:
            print("Invalid choice d00d. Enter either a Y or N.\n")

# Function to connect to the database
def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print(f"Successfully Connected To {db_name}\n")
    return db_conn, db_cursor

def welcome_message():
    wait(3, "Welcome to my database program!")

# Function to create the table
def create_table(db_cursor):
    sql = f"create table {table_name} (id integer, assignment integer, title text, due date, hours real, rating real)"
    db_cursor.execute(sql)
    print(f"Table Created: {table_name}")

# Function to drop the table
def drop_table(db_cursor):
    sql = f"drop table if exists {table_name}"

    db_cursor.execute(sql)
    print(f"\nTable Dropped: {table_name}")

# Function to insert a record into the table
def insert_record(db_cursor):
    sql = f"insert into {table_name} values (?, ?, ?, ?, ?, ?)"

    id = int(input("Enter the module ID: "))
    assignment = int(input("Enter the assignment's number: "))
    title = input("Enter the assignment's title: ")
    due = input("Enter the due date (YYYY-MM-DD): ")
    hours = float(input("Enter the estimated hours it took to complete: "))
    rating = float(input("Enter your rating (1-5): "))

    tuple_of_values = (id, assignment, title, due, hours, rating)

    db_cursor.execute(sql, tuple_of_values)
    print("\nRecord Inserted")

# Function to select without where clause
def select_all(db_cursor):
    sql = f"select * from {table_name}"

    result_set = db_cursor.execute(sql)

    # Flag to keep track of whether the records are found or not
    # I did this so I could print "None" if no records are found in the display_menu() function
    records_found = False
    for record in result_set:
        wait(2, record)
        records_found = True

    return records_found

# Function to select WITH where clause
def select_record(db_cursor):
    sql = f"select * from {table_name} where id = ?"
    id = int(input("Enter the ID of the record you would like to select: "))

    tuple_of_value = (id,)
    result_set = db_cursor.execute(sql, tuple_of_value)

    print("\nRecord Selected:")
    for record in result_set:
        wait(2, record)

# Function to update an existing record. I could make this more defensive by checking if the record exists first, but I don't think it's really necessary
def update_record(db_cursor):
    sql = f"update {table_name} set hours = ?, rating = ? where id = ?"

    id = int(input("\nEnter the ID of the record you would like to update: "))
    new_hours = float(input("Enter the new hours: "))
    new_rating = float(input("Enter the new rating: "))

    tuple_of_values = (new_hours, new_rating, id)
    db_cursor.execute(sql, tuple_of_values)

    print("\nRecord Updated")

# Function to delete an existing record
# This might cause a softlock if the record doesn't exist? That's a problem for future me
def delete_record(db_cursor):
    sql = f"delete from {table_name} where id = ?"
    
    delete_id = int(input("Enter the ID of the record you would like to delete: "))
    tuple_of_value = (delete_id,)

    if confirm_action("\nAre you sure you want to delete this record? This cannot be undone. [Y/N]: "):
        db_cursor.execute(sql, tuple_of_value)
        print("\nRecord Deleted")

# Function to display the menu for what user can do
def display_menu(db_conn, db_cursor):
    # while True loop to keep the program running until the user decides to quit
    while True:
        wait(2, "\nMenu:")
        wait(2, "Enter S to get started and create a new database")
        wait(2, "Enter C to create a new record")
        wait(2, "Enter R to retrieve data")
        wait(2, "Enter U to update a record")
        wait(2, "Enter D to delete a record")
        wait(2, "Enter Q to quit the program")
        user_input = input("\nWhat would you like to do?: ").lower()

        if user_input == "s":
            if confirm_action("This will drop any existing tables. Would you like to continue? [Y/N]: "):
                drop_table(db_cursor)
                create_table(db_cursor)        
        elif user_input == "c":
            print("Creating A New Record\n")
            insert_record(db_cursor)
        elif user_input == "r":
            print("Printing Records")
        elif user_input == "u":
            update_record(db_cursor)
        elif user_input == "d":
            delete_record(db_cursor)
        elif user_input == "q":
            break
        else:
            wait(3, "Invalid choice................. Try again.")

        db_conn.commit()
        wait(2, "\nCurrent Table:")

        # Make it so that it'll say "None" if there are no records
        records_found = select_all(db_cursor)
        if not records_found:
            print("None")
        wait(3)

def close_db(db_conn):
    db_conn.close()
    print(f"\nThe connection to {db_name} is now closed. Goodbye :(")

def main():
    db_conn, db_cursor = connect_to_db()
    welcome_message()
    display_menu(db_conn, db_cursor)
    close_db(db_conn)


if __name__ == "__main__":
    main()