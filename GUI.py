from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import requests
import os
from csv import writer
from bs4 import BeautifulSoup

# Variables
row = 2
flag = 0
counter = 0
dirPath = os.getcwd()
arr = [[0 for x in range(10)] for y in range(10)]


# Functions


def addHeader():
    global button1, row, arr, counter
    if row == 2:
        Label(frame_2, text="Table Headers").grid(row=row, column=0)
        #Label(frame_2, text="Class/id").grid(row=row, column=1)
        Label(frame_2, text="Class Name").grid(row=row, column=1)
    row += 1
    button1.pack_forget()
    arr[counter][0] = Entry(frame_2)
    arr[counter][0].grid(row=row, column=0)
    """select = ttk.Combobox(frame_2, values=["Class", "ID"])
    select.grid(row=row, column=1)
    select.bind("<<ComboboxSelected>>", selected)"""
    arr[counter][1] = Entry(frame_2)
    arr[counter][1].grid(row=row, column=1)
    row += 1
    button1.grid(row=row, column=0)
    counter += 1


def selected(Event):
    print("Selected!")


def save():
    global dirPath
    dirName = filedialog.askdirectory(
        parent=window, initialdir=dirPath, title='Select Folder')
    if dirName == "":
        return None
    else:
        dirPath = dirName
        # print(dirPath)
        cwd.destroy()
        Label(frame_5, text=dirPath + "\\").grid(row=0, column=0)


def addPages():
    # print("Clicked!")
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
    # Scraping Variables
    global counter
    url = urlentry.get()
    enclosing_div = enc_div.get()
    file_name = filename.get()
    filepath = dirPath + "/" + file_name + ".csv"
    header = [0]*10
    class_name = [0]*10
    result = [0]*counter
    for x in range(counter):
        header[x] = arr[x][0].get()
        class_name[x] = arr[x][1].get()

    # print(filepath)

    # Scraping Script
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all(class_=enclosing_div)

    with open(filepath, 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        headers = header
        csv_writer.writerow(headers)
        for div in divs:
            for x in range(counter):
                result[x] = div.find(class_=class_name[x]
                                     ).get_text().replace('\u20b9', 'Rs')
            csv_writer.writerow(result)

    # print("Exported!")


# Setting Up Window
window = Tk()
window.title("Web Scraper")
# window.geometry('600x200')

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
Label(frame_2, text="Enclosing <div> Class").grid(row=0, column=1)

e = Entry(frame_2, state="disabled")
e.grid(row=1, column=0)
e.insert(0, "Enclosing <div>")
# print(e.get())
"""select = ttk.Combobox(frame_2, values=["Class", "ID"])
select.grid(row=1, column=1)
select.bind("<<ComboboxSelected>>", selected)"""
enc_div = Entry(frame_2)
enc_div.grid(row=1, column=1)


button1 = Button(frame_2, text='Add Header', width=10, command=addHeader)
button1.grid(row=3, column=0)

# Pagination
check = BooleanVar()
check.set(FALSE)
page = Checkbutton(frame_3, text="Add pages", var=check, command=addPages)
page.grid(row=0, column=0, sticky="w")

# Export Button
cwd = Label(frame_5, text=dirPath+"\\")
cwd.grid(row=0, column=0)
filename = Entry(frame_5)
filename.insert(END, 'Default')
filename.grid(row=0, column=1)
Label(frame_5, text=".csv").grid(row=0, column=2)
export_button = Button(frame_5, text="Export as CSV", command=export)
export_button.grid(row=1, column=1, pady=10, sticky="E")
select_button = Button(frame_5, text="Select Folder", command=save)
select_button.grid(row=1, column=0, pady=10, sticky="E")

window.mainloop()
