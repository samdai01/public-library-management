"""
Database commands:
    Create and initialize, insert, view, search, update, and delete
Implemented by Sam Dai
"""

import mysql.connector
"""
Creates a new database to store book data.
"""
def create_database():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_data")
    connection.commit()
    connection.close()

"""
Creates the 3 required tables to store all books, checked out books, and on hold books.
"""
def create_tables():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = 'library_data')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title TEXT, author TEXT, year INT, isbn INT, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS checked_out (id INT AUTO_INCREMENT PRIMARY KEY, title TEXT, author TEXT, year INT, isbn INT, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS on_hold (id INT AUTO_INCREMENT PRIMARY KEY, title TEXT, author TEXT, year INT, isbn INT, name TEXT)")
    connection.commit()
    connection.close()
    
"""
Inserts a new book to the specified table. Enter information in the entry text boxes.
"""
def insert_book(title, author, year, isbn, name, table):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    
    if table == 0:
        sql = "INSERT INTO books (title, author, year, isbn, name) VALUES (%s, %s, %s, %s, %s)"
        val = (title, author, year, isbn, name)
        cursor.execute(sql, val)
    elif table == 1:
        sql = "INSERT INTO checked_out (title, author, year, isbn, name) VALUES (%s, %s, %s, %s, %s)"
        val = (title, author, year, isbn, name)
        cursor.execute(sql, val)
    elif table == 2:
        print("Test")
        sql = "INSERT INTO on_hold (title, author, year, isbn, name) VALUES (%s, %s, %s, %s, %s)"
        val = (title, author, year, isbn, name)
        cursor.execute(sql, val)
    connection.commit()
    connection.close()

"""
Views all books in catalog.
"""
def view_all():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books ORDER BY title")
    books = cursor.fetchall()
    connection.close()
    return books

"""
Views all books that are checked out.
"""
def view_checkedOut():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM checked_out ORDER BY title")
    books = cursor.fetchall()
    connection.close()
    return books

"""
Views all books that are on hold.
"""
def view_onHold():
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM on_hold ORDER BY title")
    books = cursor.fetchall()
    connection.close()
    return books

"""
Searches the catalog for a specified novel, displays all relevant novels, does not have to have all inputs filled.
"""
def search_catalog(database, title = "", author = "", year = "", isbn = "", name = ""):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = 'library_data')
    cursor = connection.cursor()
    if database == 0:
        sql = "SELECT * FROM books WHERE title = %s OR author = %s OR year = %s OR isbn = %s OR name = %s"
        val = (title, author, year, isbn, name)
    elif database == 1:
        sql = "SELECT * FROM checked_out WHERE title = %s OR author = %s OR year = %s OR isbn = %s OR name = %s"
        val = (title, author, year, isbn, name)
    elif database == 2:
        sql = "SELECT * FROM on_hold WHERE title = %s OR author = %s OR year = %s OR isbn = %s OR name = %s"
        val = (title, author, year, isbn, name)
    
    cursor.execute(sql, val)
    results = cursor.fetchall()
    
    return results   

"""
Updates a book's information.
"""
def update_book(id, newTitle, newAuthor, newYear, newISBN, newName, database):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    if database == 0:
        sql = "UPDATE books SET title = %s, author = %s, year = %s, isbn = %s, name = %s WHERE id = %s"
    elif database == 1:
        sql = "UPDATE checked_out SET title = %s, author = %s, year = %s, isbn = %s, name = %s WHERE id = %s"
    elif database == 2:
        sql = "UPDATE on_hold SET title = %s, author = %s, year = %s, isbn = %s, name = %s WHERE id = %s"
        
    val = (newTitle, newAuthor, newYear, newISBN, newName, id)
    cursor.execute(sql, val)
    connection.commit()
    connection.close()
  
"""
Deletes a book from a given table by its ISBN number.
"""  
def delete_book(isbn, database):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'test', database = "library_data")
    cursor = connection.cursor()
    if database == 0:
        cursor.execute(f"DELETE FROM books WHERE isbn = {isbn}")
    elif database == 1:
        cursor.execute(f"DELETE FROM checked_out WHERE isbn = {isbn}")
    elif database == 2:
        cursor.execute(f"DELETE FROM on_hold WHERE isbn = {isbn}")
    connection.commit()
    connection.close()
    


    
    
