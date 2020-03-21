"""
Input: Excel file as an argument.
Excel file consists of measurement results in columns.

Goal: to replace rows with duplicated frequency (column1) with 
single row with averaged values in other columns.

Output: new csv file with the same name + "_ed" addition.

Test file consists of transfer characteristics of low-pass RC-filter:
frequency | amplitude(Ch1-Ch2) | dB(Ch1-Ch2) | amplitude(Ch1) |
amplitude(Ch2) | amplitude(Ch1)-amplitude(Ch2) |

"""

import os
import sys
import pandas as pd


arguments = sys.argv

file = arguments[1]  # Take filename with patch from argument

filename, file_extension = os.path.splitext(file)  #split to path and extension

# file = "D:\\3\\test11.xlsx"  # for test without arguments

df = pd.read_excel(file, sheet_name=0, index_col=None, skiprows=0)
groupCol = df.columns[0]  # Column for grouping

print("Input data:\n", df.head())
# print(df.iloc[0:10, 0])  # test of indexing

df1 = df.groupby(groupCol).mean()  # One can use "as_index=False" - it gives additional index column
print("Output data:\n", df1.head())

df1.to_csv(filename+"_ed.csv", sep=";")  # Save to csv, semicolon is nice for opening in Excel
