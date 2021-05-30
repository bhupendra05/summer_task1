import pandas

ds=pandas.read_csv("SalaryData.csv")
x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary']

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model=model.fit(x,y)

import joblib
joblib.dump(model,'trained_model.pk1')
