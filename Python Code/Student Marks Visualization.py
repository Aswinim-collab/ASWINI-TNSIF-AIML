import matplotlib.pyplot as plt

# Student names and marks
students = ["Arun", "Bala", "Divya", "Kavi", "Nisha",
            "Ravi", "Siva", "Priya", "Kumar", "Anu"]

marks = [85, 72, 91, 68, 78, 88, 35, 95, 55, 45]

# Bar Chart
plt.bar(students, marks)

plt.title("Student Python Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()


# Performance categories
excellent = sum(80 <= mark <= 100 for mark in marks)
good = sum(60 <= mark <= 79 for mark in marks)
average = sum(40 <= mark <= 59 for mark in marks)
needs_improvement = sum(mark < 40 for mark in marks)

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
counts = [excellent, good, average, needs_improvement]

# Pie Chart
plt.pie(counts, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")
plt.show()
