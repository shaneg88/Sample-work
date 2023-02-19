# import sqlite3
import sqlite3

# create database file
db = sqlite3.connect("ebookstore.db")

# create cursor object
cursor = db.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS 
books(id INTEGER PRIMARY KEY,
title TEXT,
author TEXT,
qty INTEGER,
UNIQUE(id))
""")

db.commit()

# create function for adding new books to the database with input from the user
# offers an error message if incorrect details are used
def add_book():
    print("Please enter the details of the book to be added\n")
    new_id = input("Please enter the book id(numbers only): ")
    while True:
        if len(new_id) != 4:
            print("id must be 4 digits long")
            new_id = input("Please enter the book id(numbers only): ")
            continue
        else:
            break

    new_title = input("Please enter book title: ")
    new_author = input("Please enter author of book: ")
    new_qty = input("Please enter quantity(numbers only): ")

    try:
        cursor.execute("INSERT INTO books(id, title, author, qty) VALUES(?, ?, ?, ?)",
                       (new_id, new_title, new_author, new_qty))
        db.commit()
        print("New book successfully added.\n")
    except Exception as e:
        db.rollback()
        print("There was an error with the details entered please retry")

# create function for updating book using the id as the search code
# user is asked to pick what should be updated and to what it should be changed
def update_book():
    update_id = input("What is the id of the book to update: ")
    update_field = input("Which field would you like to update(id, title, author, qty): ").lower()

    try:
        if update_field == "id":
            update_info = input("What is the new id(numbers only): ")
            while True:
                if len(update_info) != 4:
                    print("id must be 4 digits long")
                    update_info = input("Please enter the book id(numbers only): ")
                    continue
                else:
                    break
            cursor.execute("UPDATE books SET id = ? WHERE id = ?", (update_info, update_id))
            db.commit()
            print("Book updated")
        elif update_field == "title":
            update_info = input("What is the new title: ")
            cursor.execute("UPDATE books SET title = ? WHERE id = ?", (update_info, update_id))
            db.commit()
            print("Book updated")
        elif update_field == "author":
            update_info = input("What is the new author: ")
            cursor.execute("UPDATE books SET author = ? WHERE id = ?", (update_info, update_id))
            db.commit()
            print("Book updated")
        elif update_field == "qty":
            update_info = input("What is the new data(numbers only): ")
            cursor.execute("UPDATE books SET qty = ? WHERE id = ?", (update_info, update_id))
            db.commit()
            print("Book updated")
        else:
            print("Incorrect choice")

    
    except Exception as e:
        db.rollback()
        print("There was an error with the details entered please retry")

# create function to delete books from table
# user is asked to enter id of book to be deleted and wether they are sure to proceed
def delete_book():
    delete_id = input("Please input the id of the book to be deleted: ")

    cursor.execute("SELECT * FROM books WHERE id = ? ", (delete_id,))
    book = cursor.fetchone()
    print(book)
    if input("Are you sure you wish to proceed (y/n): ").lower() == "y":
        cursor.execute("DELETE FROM books WHERE id = ?", (delete_id,))
        db.commit()
        print("Book deleted")
    else:
        print("Returning to main menu")
        pass

# create function to search the database based on a books id
# then print the relevant info about the book
def search_book():
    search_id = input("What is the id of the book you wish to search for: ")

    cursor.execute("SELECT * FROM books WHERE id = ?", (search_id,))
    book = cursor.fetchone()
    print(book)

# create an extra function to show all books in the database 
# for user simplicity
def show_all():
    cursor.execute("SELECT * FROM books")
    for row in cursor:
        print(row)


# create user menu for using the program
while True:
    output = "-----Main Menu-----\n"
    output += "1 - Enter book\n"
    output += "2 - Update book\n"
    output += "3 - Delete book\n"
    output += "4 - Search books\n"
    output += "5 - show all books\n"
    output += "0 - Exit"
    print(output)
    try: 
        choice = int(input("Please make your selection: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            update_book()
        elif choice == 3:
            delete_book()
        elif choice == 4:
            search_book()
        elif choice == 5:
            show_all()
        elif choice == 0:
            db.close()
            exit()
        else:
            print("Incorrect choice")

    except ValueError:
        print("Incorrect input made")
        continue