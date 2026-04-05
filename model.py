import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv('cleaned_loan_data.csv')

x= df[['Gender' , 'Married' , 'Dependents' , 'Education' , 'Self_Employed' , 'ApplicantIncome' , 'CoapplicantIncome' , 'LoanAmount' ,'Loan_Amount_Term' , 'Credit_History' ,'Property_Area']]


y = df['Loan_Status']


model = DecisionTreeClassifier()

model.fit(x,y)


fh = open('trained_model.pkl', 'wb')
pickle.dump(model, fh)
fh.close()