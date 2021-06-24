from tkinter import *

from tkinter import filedialog

import pandas as pd


def generate_table(file_name):
    df = pd.read_csv(file_name)

    writer = pd.ExcelWriter('~/Desktop/table.xlsx')

    df.to_excel(writer, index=False)

    writer.save()


def browse_files():
    file_name = filedialog.askopenfilename(initialdir='/',
                                           title="Select a csv file",
                                           filetypes=(("Text files",
                                                       "*.txt"),
                                                      ("all files",
                                                       "*.*")))
    label_file_explorer.configure(text="File opened: "+file_name)
    generate_table(file_name)


window = Tk()

window.title('File Explorer')

window.geometry("900x500")

window.config(background="white")

label_file_explorer = Label(window,
                            text="Hey Siju!",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse File", height=3, width=15,
                        command=browse_files)


label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)

window.mainloop()
