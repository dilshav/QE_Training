# import pandas
import pandas as pd

# Create a dictionary to hold our data
data = {
  "X": [1, 2, 3, 4, 5],
  "Y": [9, 8, 7, 6, 5],
  "Z": [10, 12, 8, 4, 3]
}

# Create a new DataFrame using our dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
#print only one serries
print(df["X"])
print(df["Z"][2])
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")