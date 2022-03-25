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
