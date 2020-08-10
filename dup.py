"""
Input: Excel file as an argument.
Excel file consists of measurement results in columns.

Goal: to replace rows with duplicated frequency (column 1) with 
single row with averaged values in other columns.

Output: new csv file with new name  "oldname_ed".

Test file consists of transfer characteristics of low-pass RC-filter:
frequency | amplitude(Ch1-Ch2) | dB(Ch1-Ch2) | amplitude(Ch1) |
amplitude(Ch2) | amplitude(Ch1)-amplitude(Ch2) |

"""

import os
import sys
import pandas as pd
import tkinter
from tkinter import filedialog, messagebox


def show_res(text):
	tkinter.messagebox.showinfo("Results", text)


def rem_dup(file):
	print(file, type(file))
	filename, file_extension = os.path.splitext(file)
	print(file_extension)
	if file_extension in ('.xlsx', '.xls'):
		df = pd.read_excel(file, sheet_name=0, index_col=None, skiprows=0)
		inputdata = "Input data:\n" + df.head(10).to_string()
		show_res(inputdata)
		groupCol = df.columns[0]  # Column for grouping
		df1 = df.groupby(groupCol).mean()  # "as_index=False"-additional index column
		outputdata = "Output data:\n" + df1.head(10).to_string()
		show_res(outputdata)
		df1.to_csv(filename+"_ed.csv", sep=";")  # semicolon is nice for opening in Excel
	else:
		show_res("The file is not excel file. Please provide excel file.")

def clicked():
	t = tkinter.filedialog.askopenfilename()
	rem_dup(t)

app = tkinter.Tk()
app.geometry('300x200')
app.title('Remove duplicates in xls')

header = tkinter.Label(app, text="This script removes rows with duplicated values\n in first column of xls file\n and makes one row with mean values.\n\n Please, select Excel file (*.xls, *.xlsx):") # , fg="blue", font=("Arial Bold", 16))
header.pack(side="top", ipady=10)

open_files = tkinter.Button(app, text ="Choose file...", command=clicked)
open_files.pack(fill='x')
app.mainloop()