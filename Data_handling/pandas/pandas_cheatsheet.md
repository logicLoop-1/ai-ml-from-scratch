# Pandas Cheatsheet

## Creating a DataFrame
| Code | Result |
|---|---|
| `pd.DataFrame(dict)` | dict of lists → table (keys = columns) |
| `pd.DataFrame(data, index=[...])` | custom row labels instead of default 0,1,2... |
| `pd.read_csv("file.csv")` | load from CSV |
| `pd.read_csv("file.csv", index_col="name")` | load, using a column as the index |
| `pd.read_json("file.json")` | load from JSON |
| `df.to_csv("out.csv")` | write DataFrame back out to CSV |

## Inspecting Data (always do this first on new data)
| Code | Result |
|---|---|
| `df.head()` / `df.tail(n)` | first/last rows |
| `df.shape` | (rows, columns) |
| `df.info()` | column names, dtypes, non-null counts — spot missing data fast |
| `df.describe()` | mean, std, min/max, quartiles (numeric columns only) |
| `df.columns` | list of column names |
| `df.dtypes` | data type per column |

## Selecting Data
| Code | Result |
|---|---|
| `df["col"]` | one column (Series) |
| `df[["col1", "col2"]]` | multiple columns (note double brackets) |
| `df.iloc[0]` | row by INTEGER POSITION |
| `df.iloc[0:2]` | rows by position, slice |
| `df.loc["label"]` | row by INDEX LABEL |
| `df.loc["label", "col"]` | specific cell by label |
| `df.loc["label", ["col1","col2"]]` | specific columns for one labeled row |

**`.iloc` = position (like list indexing). `.loc` = label (index/column names).**
`.loc["Ali"]` only works if `"Ali"` is actually the index — not just a value inside a column.

## Filtering Rows
| Code | Result |
|---|---|
| `df[df["age"] > 20]` | single condition |
| `df[(df["age"]>20) & (df["gpa"]>3.3)]` | multiple conditions — use `&`/`\|`, NOT `and`/`or`, and wrap each condition in parentheses |
| `df[df["name"] == "Ali"]` | exact match |
| `result.empty` | check if a filter returned zero rows |

## Adding / Modifying / Dropping
| Code | Result |
|---|---|
| `df["new_col"] = [...]` | new column, manually specified values |
| `df["new_col"] = df["age"] >= 18` | new column, COMPUTED (vectorized) |
| `pd.concat([df, new_row_df])` | add one or more new rows |
| `df.drop("col", axis=1)` | drop a column |
| `df.drop(0, axis=0)` | drop a row |

## Missing Data
| Code | Result |
|---|---|
| `df.isnull()` | True/False grid showing missing values |
| `df.isnull().sum()` | count of missing values PER COLUMN — run this early on any dataset |
| `df.dropna()` | drop rows with any missing value |
| `df.fillna(0)` | replace missing values with 0 |
| `df["col"].fillna(df["col"].mean())` | fill missing values with that column's mean |

## GroupBy
| Code | Result |
|---|---|
| `df.groupby("major")["gpa"].mean()` | average gpa, per group |
| `df.groupby("major").agg({"gpa":"mean","age":"max"})` | multiple aggregations at once |

Reads as: "group rows by this label, then summarize each group."

## Sorting
| Code | Result |
|---|---|
| `df.sort_values("gpa")` | ascending |
| `df.sort_values("gpa", ascending=False)` | descending |
| `df.sort_values(["major","gpa"])` | sort by multiple columns |

## Custom Logic — `.apply()`
```python
df["grade"] = df["gpa"].apply(lambda g: "A" if g >= 3.5 else "B" if g >= 3.0 else "C")
```
Runs a function/lambda across every value in a column, producing a new column.

## Merging DataFrames
```python
pd.merge(df1, df2, on="student_id")
```
Combines two DataFrames using a shared column as the key — same idea as a SQL JOIN.
