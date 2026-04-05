from flask import Flask,render_template , request
import pickle

model = pickle.load(open('trained_model.pkl','rb'))
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def lone():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        Gender = int(request.form.get('Gender'))
        Married = int(request.form.get('Married'))
        Dependents = int(request.form.get('Dependents'))
        Education = int(request.form.get('Education'))
        Self_Employed= int(request.form.get('Self_Employed'))
        Applicant_Income = int(request.form.get('ApplicantIncome'))
        CoapplicantIncome = int(request.form.get('CoapplicantIncome'))
        LoanAmount = int(request.form.get('LoanAmount'))
        Loan_Amount_Term = int(request.form.get('Loan_Amount_Term'))
        Credit_History = float(request.form.get('Credit_History'))
        Property_Area = int(request.form.get('Property_Area'))

        lone_arr = model.predict([[ Gender , Married , Dependents , Education ,  Self_Employed , Applicant_Income , CoapplicantIncome , LoanAmount , Loan_Amount_Term , Credit_History ,   Property_Area ]])
        lone = lone_arr[0]
        if lone == 0:
            lone = "No"
        elif lone == 1:
            lone = "Yes"
        return  render_template('result.html' , lone_value = lone)



if __name__ == '__main__':
    app.run(debug=True)