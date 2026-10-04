import pandas as pd

# Student data
data = {
    "Name": ["Arun", "Bala", "Divya", "Kavi", "Nisha", "Ravi", "Siva", "Priya"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE", "IT", "CSE"],
    "Marks": [85, 72, 91, 68, 78, 88, 55, 95],
    "Attendance": [90, 75, 85, 92, 78, 88, 70, 95]
}

df = pd.DataFrame(data)

# Display first 5 students
print("First 5 Students:")
print(df.head())

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Students who scored more than 75
print("\nStudents with marks greater than 75:")
print(df[df["Marks"] > 75])

# Students whose attendance is below 80%
print("\nStudents with attendance below 80%:")
print(df[df["Attendance"] < 80])

# Sort students based on marks
print("\nStudents sorted by marks:")
print(df.sort_values("Marks"))
