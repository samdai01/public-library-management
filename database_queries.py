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