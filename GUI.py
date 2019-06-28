from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from bs4 import BeautifulSoup as soup

# Variables
row = 1
flag = 0


# Functions


def addHeader():
    global button1, row
    row += 1
    button1.pack_forget()
    Entry(frame_2).grid(row=row, column=0)
    select = ttk.Combobox(frame_2, values=["Class", "ID"])
    select.grid(row=row, column=1)
    select.bind("<<ComboboxSelected>>", selected)
    Entry(frame_2).grid(row=row, column=2)
    row += 1
    button1.grid(row=row, column=0)


def selected(Event):
    print("Selected!")


def addPages():
    print("Clicked!")
    global check, flag
    if check.get() == TRUE:
        Label(frame_4, text="No. of pages").grid(row=1, column=0)
        Entry(frame_4).grid(row=1, column=1)
        Label(frame_4, text="Class of 'Next' button").grid(row=1, column=2)
        Entry(frame_4).grid(row=1, column=3)
        flag = 1
    elif check.get() == FALSE and flag == 1:
        Label(frame_4, text="No. of pages").grid(row=1, column=0)
        Entry(frame_4, state='disabled').grid(row=1, column=1)
        Label(frame_4, text="Class of 'Next' button").grid(row=1, column=2)
        Entry(frame_4, state='disabled').grid(row=1, column=3)
        flag = 0


def export():
    print("Exported!")


# Setting Up Window
window = Tk()
window.title("Web Scraper")
# window.geometry('800x600')

# Frames
frame_1 = Frame(window)
frame_1.pack()
frame_2 = Frame(window)
frame_2.pack()
frame_3 = Frame(window)
frame_3.pack()
frame_4 = Frame(window)
frame_4.pack()
frame_5 = Frame(window)
frame_5.pack()

# Menubar


# URL Entry
Label(frame_1, text="Enter URL").pack(side="left")
urlentry = Entry(frame_1, width=80)
urlentry.pack(side="left")

# Element Entry
Label(frame_2, text="Table Headers").grid(row=0, column=0)
Label(frame_2, text="Class/id").grid(row=0, column=1)
Label(frame_2, text="Name(Class/id)").grid(row=0, column=2)

Entry(frame_2).grid(row=1, column=0)
select = ttk.Combobox(frame_2, values=["Class", "ID"])
select.grid(row=1, column=1)
select.bind("<<ComboboxSelected>>", selected)
Entry(frame_2).grid(row=1, column=2)
button1 = Button(frame_2, text='Add Header', width=10, command=addHeader)
button1.grid(row=2, column=0)

# Pagination
check = BooleanVar()
check.set(FALSE)
page = Checkbutton(frame_3, text="Add pages", var=check, command=addPages)
page.grid(row=0, column=0, sticky="w")

# Export Button
export_button = Button(frame_5, text="Export as CSV", command=export)
export_button.grid(row=0, column=0, pady=10, sticky="E")

window.mainloop()
