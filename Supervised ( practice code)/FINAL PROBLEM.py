from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Dataset
X = np.array([
    [20,15000],
    [22,18000],
    [25,22000],
    [28,30000],
    [30,35000],
    [32,40000],
    [35,45000],
    [38,50000],
    [40,55000],
    [45,60000]
])

y = np.array([0,0,0,1,1,1,1,1,1,1])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# New Customer
new = [[27,28000]]

print("Logistic Prediction:", lr.predict(new))
print("Decision Tree Prediction:", dt.predict(new))

# Accuracy
print("Logistic Accuracy:", accuracy_score(y_test, lr_pred))
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))
