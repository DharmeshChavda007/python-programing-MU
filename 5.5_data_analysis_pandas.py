# Write a program to perform basic data analysis using Pandas Data Frame.

import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Rahul", "Amit", "Priya", "Neha", "Raj"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

# Display complete DataFrame
print("DataFrame:")
print(df)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display shape
print("\nShape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display total number of elements
print("\nSize:")
print(df.size)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display statistical description
print("\nStatistical Description:")
print(df.describe())

# Display maximum and minimum values
print("\nMaximum Values:")
print(df.max())

print("\nMinimum Values:")
print(df.min())
