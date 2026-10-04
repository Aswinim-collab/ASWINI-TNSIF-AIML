import numpy as np
from sklearn.linear_model import LogisticRegression

# Data
X = np.array([
    [20,15000],
    [22,18000],
    [25,25000],
    [28,30000],
    [30,35000],
    [35,40000],
    [40,50000],
    [45,60000]
])

y = np.array([0,0,0,1,1,1,1,1])

# Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
print("Prediction:", model.predict([[27,28000]]))
