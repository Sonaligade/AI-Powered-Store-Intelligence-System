from sklearn.ensemble import IsolationForest

model = IsolationForest()

def detect(x):
    return model.fit_predict([x])
