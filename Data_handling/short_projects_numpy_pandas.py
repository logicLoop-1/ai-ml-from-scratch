#1. Grade Calculator (array-based) using Numpy
import numpy as np
arr = np.array([[19, 13, 18], #student1
            [16, 15, 20], #student2
            [7, 10, 15]]) #student3
student_avg = arr.mean(axis = 1)
print(f"each students average is: {student_avg}") #each student avg per row
test_avg = arr.mean(axis = 0)
print(f"each test average is: {test_avg}") # each test avg per column
high_score = arr.max()
low_score = arr.min()
print (f"high score is {high_score}")
print(f"low score is {low_score}")
best_student_index = student_avg.argmax()
print(f"best student index = {best_student_index} -> average: {student_avg[best_student_index]}")
student_passing = student_avg[student_avg>=15]
print(f"passing student average: {student_passing}")
passing_indices = np.where(student_avg>=15)[0]
print(f"passing student index: {passing_indices}")
#2. image gray scale simulator 
image  = np.array([          #5x5 grid representation of a tiny image 0=pure black 255 = white
    [50, 20, 180, 200, 255],
    [30, 60, 90, 150, 220],
    [10, 40, 70, 100, 180],
    [5, 20, 50, 80, 160],
    [0, 15, 35, 60, 140],
])
def brighten(image, amount):
    brightened = image+amount
    return np.clip(brightened, 0, 255)
brightened = brighten(image, 30)
print(brightened)
def average_brightness(image):
    return image.mean()
def threshold(image, cutoff):
    return np.where(image>= cutoff, 255, 0)
bw_image = threshold(image, 100)
average_brightness = average_brightness(image)
print(bw_image)
print(average_brightness)
#3. Personal Expense Tracker
import pandas as pd
data = {
    "date": ["16-09-26", "25-08-26", "15-07-26", "25-08-26", "12-09-26"], 
    "category": ["foods", "travel", "beauty", "foods", "travel"],
    "amount" : [5600, 6500, 6700, 8800, 1200]
}
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%y")
print(df)
def add_new(df, date, category, amount):
    new_row = pd.DataFrame([{"date": date, "category": category, "amount": amount}])
    return pd.concat([df, new_row], ignore_index= True)
df = add_new(df, "21-09-26", "fees", 7800)
print (df)
total_by_category = df.groupby("category")["amount"].sum()
print(total_by_category)
most_expensive = df.loc[df["amount"].idxmax()]
print("most_expersive is: ", most_expensive)
big_expenses = df[df["amount"]>7000]
print("big expenses are: ", big_expenses)
# Class Performance Analyzer
df1 = pd.read_csv("students.csv")
print(df1.isnull().sum())
avg_gpa_by_major = df1.groupby("major")["gpa"].mean()
print(avg_gpa_by_major)
sortedDf1 = df1.sort_values("gpa")
print(sortedDf1)
num_students = len(df1)
num_majors = df1["major"].nunique()
overall_avg = df1["gpa"].mean()
print(f"{num_students} students, {num_majors} majors, average GPA: {overall_avg:.2f}")