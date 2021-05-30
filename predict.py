import joblib
model=joblib.load("trained_model.pk1")

exp=int(input("Enter Year Of Experience:"))
pred=model.predict([[exp]])
print("Expected Salary is : ",round(pred[0],2),"INR.")