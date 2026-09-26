import pandas as pd

# Q1: Create a DataFrame from a dictionary with a custom index (not default 0,1,2...).
data = {
    "name": ["patrick", "spongebob", "squidward"],
    "age": [33, 55, 32]
}
df = pd.DataFrame(data, index=["employee 1", "employee 2", "employee 3"])
print(df)

# Q2: Add a new column with manually specified values.
df["job"] = ["waiter", "chef", "casheir"]
print(df)

# Q3: Add a single new row to an existing DataFrame using pd.concat().
new_row = pd.DataFrame([{"name": "Sandy", "age": 43, "job": "engineer"}], index=["employee 4"])
df = pd.concat([df, new_row])
print(df)

# Q4: Add multiple new rows at once using pd.concat().
new_rows = pd.DataFrame([{"name": "menka", "age": 20, "job": "cs"},
                         {"name": "hema", "age": 40, "job": "doctor"}],
                        index=["employee 5", "employee 6"])
df = pd.concat([df, new_rows])
print(df)

# Q5: Load a real CSV file and select specific columns.
df1 = pd.read_csv("students.csv")
print(df1)
print(df1[["name", "gpa"]])
print(df1.loc[0])   # row at index label 0

# Q6: Load a CSV using a meaningful column as the index instead of default numbers.
df = pd.read_csv("students.csv", index_col="name")
print(df)
print(df[["major", "gpa"]])   # name is always shown, since it's now the index

# Q7: Select a specific row by its label, then only specific columns from that row.
print(df.loc["Nida"])
print(df.loc["Nida", ["gpa", "city"]])

# Q8: Select the first N rows by position, using iloc slicing.
print(df.iloc[0:5])

# Q9: Look up a row safely, handling the case where it doesn't exist.
df2 = pd.read_csv("students.csv", index_col="name")
student = input("enter student name: ")

try:
    print(df2.loc[student])
except KeyError:
    print(f"{student} not found")
# Q10: Filter rows that match a single condition.
strong_student = df[df["gpa"] >= 3.5]
print(strong_student)
