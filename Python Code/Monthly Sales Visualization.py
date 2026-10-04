import matplotlib.pyplot as plt

# Monthly sales data
months = ["January", "February", "March", "April", "May", "June"]
sales = [25000, 30000, 28000, 35000, 40000, 38000]

# Line Chart
plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.show()

# Bar Chart
plt.bar(months, sales, label="Monthly Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.show()
