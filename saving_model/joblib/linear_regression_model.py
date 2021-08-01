import pandas as pd
import numpy as np

from scipy.stats import norm
from collections import Counter
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('D:\Learnbay\ML\ML_New\Linear Regression\petrol_consumption.csv')

X = dataset[['Petrol_tax','Average_income','Population_Driver_licence(%)']]#'Petrol_tax','Paved_Highways'
y = dataset['Petrol_Consumption']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=13)


regressor = LinearRegression(fit_intercept=True)
regressor.fit(X_train, y_train)

print(regressor.coef_)
y_pred = regressor.predict(X_train)
df = pd.DataFrame({'Actual': y_train, 'Predicted': y_pred})
print(df)