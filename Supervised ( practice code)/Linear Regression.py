import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([20000,25000,30000,35000,40000,45000,50000,55000])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
print("Salary for 5 years:", model.predict([[5]]))
