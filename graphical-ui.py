"""
Graphical UI Implementation of the library database.
Implemented by Sam Dai
Consists of 5 entry textboxes, 9 buttons, and three text windows for viewing Data.
Features include: 
    Viewing library catalog
    Searching through catalog
    Adding a new book to collection.
    Updating information for a selected book.
    Deleting the selected novel.
    Checking a novel out.
    Checking a novel in.
    Placing a hold on an object.
The all_books table has ID 0
The checked_out table has ID 1
The on_hold table has ID 2
Updated project can be found at github.com/samdai01/library
"""

from tkinter import *
import database_queries


window = Tk()

window.wm_title("Library Database")

program_title = StringVar()
program_title.set("Library Database Program. Made by Sam Dai")
program = Label(window, textvariable = program_title)
program.grid(row = 0, column = 9, columnspan = 2, rowspan = 2)

titleText = StringVar()
titleText.set("Title:")
title = Label(window, textvariable = titleText, width = 5)
title.grid(row = 0, column = 0)

titleInput = StringVar()
titleIn = Entry(window, textvariable = titleInput, width = 32)
titleIn.grid(row = 0, column = 1)

yearText = StringVar()
yearText.set("Year:")
year = Label(window, textvariable=yearText, width = 5)
year.grid(row = 1, column = 0)

yearInput = StringVar()
yearIn = Entry(window, textvariable = yearInput, width = 32)
yearIn.grid(row = 1, column = 1)

authorText = StringVar()
authorText.set("Author:")
author = Label(window, textvariable = authorText, width = 7)
author.grid(row = 0, column = 3)

authorInput = StringVar()
authorIn = Entry(window, textvariable = authorInput, width = 30)
authorIn.grid(row = 0, column = 4)

isbnText = StringVar()
isbnText.set("ISBN:")
isbn = Label(window, textvariable = isbnText, width = 7)
isbn.grid(row = 1, column = 3)

isbnInput = StringVar()
isbnIn = Entry(window, textvariable = isbnInput, width = 30)
isbnIn.grid(row = 1, column = 4)

nameText = StringVar()
nameText.set("Name:")
name = Label(window, textvariable=nameText)
name.grid(row = 0, column = 6)