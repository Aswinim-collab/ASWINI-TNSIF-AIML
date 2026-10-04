from sklearn.ensemble import RandomForestClassifier

X = [
    [22,2,500],
    [25,5,600],
    [30,1,800],
    [35,8,550],
    [40,10,500],
    [28,3,900],
    [45,12,650],
    [32,2,850]
]

y = [1,0,1,0,0,1,0,1]

model = RandomForestClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[29,4,700]]))
