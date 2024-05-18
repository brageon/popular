import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
# Joblib not pickle. It can store large np arrays
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(url, sep=';')
# quality, fixed acidity, volatile acidity, citric acid
# residual sugar, chlorides, free sulfur dioxide
# total sulfur dioxide, density, pH, sulphates, alcohol
y = data.quality 
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=0.2, random_state=123, stratify=y)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
pipeline = make_pipeline(preprocessing.StandardScaler(),
RandomForestRegressor(n_estimators=100, random_state=123))
# print(pipeline.get_params()), clf.best_params_
hyperparameters = { 'randomforestregressor__max_features' : 
['sqrt', 'log2'], 'randomforestregressor__max_depth': 
[5, 3, 1]}
# Cross-validation is a process for reliably estimating the 
# performance of a method for building a model.  
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
# Save model for future use
joblib.dump(clf, 'rf_regressor.pkl')
clf2 = joblib.load('rf_regressor.pkl')
clf2.predict(X_test)