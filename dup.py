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


arguments = sys.argv

if len(arguments) > 1:

	file = arguments[1]  # Take filename with patch from argument
	filename, file_extension = os.path.splitext(file)
	
	if file_extension in ('.xlsx', '.xls'):
		df = pd.read_excel(file, sheet_name=0, index_col=None, skiprows=0)
		print("Input data:\n", df.head())

		groupCol = df.columns[0]  # Column for grouping

		df1 = df.groupby(groupCol).mean()  # "as_index=False"-additional index column
		print("Output data:\n", df1.head())

		df1.to_csv(filename+"_ed.csv", sep=";")  # semicolon is nice for opening in Excel
	else:
		print("The file ", file, "is not excel file. Please provide excel file." )
else:
	print("No arguments!\nPlease, provide excel filename as an argument")