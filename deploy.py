import streamlit as st
import joblib
loaded_model=joblib.load('logistic_regression_model.pkl')
print(loaded_model)
st.title("logistic regression")
#['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
#'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
#'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
#'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
#'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'] 
gender=st.radio("Select Gender",['Male','Female'])
SeniorCitizen=st.radio("Is the person a SeniorCitizen?",['Yes','No'])
if SeniorCitizen == "Yes":
    SeniorCitizen=1
else:
    SeniorCitizen=0
Partner=st.radio("Do you have a partner",['Yes','No'])
Dependents=st.radio("Do you have children or your parents",['Yes','No'])
tenure=st.number_input("Enter a number of months you have been using our subcription", min_value=0, max_value=100, value=10)
PhoneService=st.radio("Are you using a phone service",['Yes','No'])
MultipleLines=st.radio("Are you using multiple lines?",['Yes','No','No phone service'])
InternetService=st.radio("which internet service ?",['DSL','Fiber optic','No'])
OnlineSecurity=st.radio("Do you have an antivirus?",['Yes','No','No internet service'])
if OnlineSecurity != 'No internet service':
    DeviceProtection=st.radio("Do you have any means of Device Protection?",['Yes','No','No internet service'])
    TechSupport=st.radio("Do you have any Tech Support?",['Yes','No','No internet service'])
    StreamingTV=st.radio("Do you Stream on TV?",['Yes','No','No internet service'])
    StreamingMovies=st.radio("Do you Stream movies?",['Yes','No','No internet service'])
else:
    DeviceProtection,TechSupport,StreamingTV,StreamingMovies = ['No internet service']*4
Contract=st.radio("What is the type of service you have?",['Month-to-month','One year','Two year'])
PaperlessBilling=st.radio("was it a Paperless Billing?",['Yes','No'])
PaymentMethod=st.radio("What was the payment method used ?",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
MonthlyCharges=st.number_input("Enter the often monthly charges", min_value=0.0, max_value=10000.0, value=1.5, step=0.01)
TotalCharges=st.number_input("Enter the often Total Charges", min_value=0.0, max_value=100000.0, value=1.5, step=0.01)


