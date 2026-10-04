import numpy as np

# Marks of 10 students
marks = np.array([85, 72, 90, 65, 78, 92, 55, 88, 70, 81])

# Total marks
print("Total Marks:", np.sum(marks))

# Average marks
print("Average Marks:", np.mean(marks))

# Highest and lowest marks
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Marks greater than 75
print("Marks greater than 75:", marks[marks > 75])
