from sklearn.tree import DecisionTreeClassifier

# Encode manually
# Sunny=0, Rainy=1, Cloudy=2
# Hot=0, Cool=1

X = [
    [0,0],
    [0,1],
    [1,1],
    [1,0],
    [2,0],
    [2,1],
    [0,0],
    [1,1]
]

y = [0,1,1,0,1,1,0,1]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[0,1]]))
