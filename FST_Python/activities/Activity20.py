# Reading Excel Files
# Activity 20
# Using Pandas:
# Use pandas to read data the Excel file
# Print the number of rows and columns
# Print the data in the emails column only
# Sort the data based on FirstName in ascending order and print the data
# Hint: You can use DataFrame.shape to get the number of rows and columns
import pandas as pd
df=pd.read_excel("C:/Users/DilshaRajV/OneDrive - IBM/Desktop/FST_Python/details.xlsx", sheet_name="Sheet1")
print(df)
rows, columns = df.shape
print(f"No. of rows: {rows}, No of columns: {columns}")
print(f"Emails are: {df["Email"]}")
print(pd.sort_values(df["FirstName"]))