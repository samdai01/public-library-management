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

nameInput = StringVar()
nameIn = Entry(window, textvariable=nameInput, width = 32)
nameIn.grid(row = 0, column = 7)

onhold_window = Listbox(window, height = 12, width = 40, exportselection=False)
onhold_window.grid(row = 2, column = 0, rowspan = 6, columnspan = 2, pady = (10, 0), padx = (5, 0))

onhold_scrollbar = Scrollbar(window)
onhold_scrollbar.grid(row = 2, column = 2, rowspan = 6, padx = (5, 5))
onhold_scrollbar.configure(command = onhold_window.yview)
onhold_window.configure(yscrollcommand = onhold_scrollbar.set)

checkout_window = Listbox(window, height = 12, width = 40, exportselection=False)
checkout_window.grid(row = 2, column = 3, rowspan = 6, columnspan = 2, pady = (10, 0))

checkout_scrollbar = Scrollbar(window)
checkout_scrollbar.grid(row = 2, column = 5, rowspan = 6, padx = (5, 5))
checkout_scrollbar.configure(command = checkout_window.yview)
checkout_window.configure(yscrollcommand = checkout_scrollbar.set)


allbooks_window = Listbox(window, height = 12, width = 40, exportselection=False)
allbooks_window.grid(row = 2, column = 6, rowspan = 6, columnspan = 2, pady = (10, 0))

allbooks_scrollbar = Scrollbar(window)
allbooks_scrollbar.grid(row = 2, column = 8, rowspan = 6, padx = (5, 5))
allbooks_scrollbar.configure(command = allbooks_window.yview)
allbooks_window.configure(yscrollcommand = allbooks_scrollbar.set)

holdText = StringVar()
holdText.set("On Hold")
hold = Label(window, textvariable = holdText, width = 10)
hold.grid(row = 8, column = 0, columnspan = 2)

checkout_text = StringVar()
checkout_text.set("Checked Out")
checkout = Label(window, textvariable = checkout_text, width = 10)
checkout.grid(row = 8, column = 3, columnspan = 2)

all_text = StringVar()
all_text.set("Main View")
view = Label(window, textvariable = all_text, width = 10)
view.grid(row = 8, column = 6, columnspan = 2)

viewAll = Button(window, text = "View All", command = view_command)
viewAll.grid(row = 2, column = 9)
viewAll.config(width = 12)

searchEntry = Button(window, text = "Search Entry", command = search_command)
searchEntry.grid(row = 3, column = 9)
searchEntry.config(width = 12)

addEntry = Button(window, text = "Add Entry", command = add_command)
addEntry.grid(row = 4, column = 9)
addEntry.config(width = 12)

update = Button(window, text = "Update", command = update_command)
update.grid(row = 5, column = 9)
update.config(width = 12)

delete = Button(window, text = "Delete", command = delete_command)
delete.grid(row = 6, column = 9)
delete.config(width = 12)

close = Button(window, text = "Close", command = window.destroy)
close.grid(row = 7, column = 9)
close.config(width = 12)

check_out = Button(window, text = "Check Out", command = check_out_command)
check_out.grid(row = 2, column = 10)
check_out.config(width = 12)

check_in = Button(window, text = "Check In", command = check_in_command)
check_in.grid(row = 3, column = 10)
check_in.config(width = 12)

place_hold = Button(window, text = "Place Hold", command = place_hold_command)
place_hold.grid(row = 4, column = 10)
place_hold.config(width = 12)

allbooks_window.bind("<<ListboxSelect>>", get_selected_book)
checkout_window.bind("<<ListboxSelect>>", get_selected_book)
onhold_window.bind("<<ListboxSelect>>", get_selected_book)

window.mainloop()