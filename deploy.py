import streamlit as st
import joblib
import pandas as pd

model = joblib.load('logistic_regression_model.pkl')
print(model)

st.title("Logistic Regression")

gender_map = {'Male': 0, 'Female': 1}
senior_citizen_map = {'Yes': 1, 'No': 0}
partner_map = {'Yes': 1, 'No': 0}
dependents_map = {'Yes': 1, 'No': 0}
phone_service_map = {'Yes': 1, 'No': 0}
multiple_lines_map = {'Yes': 1, 'No': 0, 'No phone service': 2}
internet_service_map = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
online_security_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
device_protection_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
tech_support_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
streaming_tv_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
streaming_movies_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
paperless_billing_map = {'Yes': 1, 'No': 0}
payment_method_map = {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}

gender = gender_map[st.radio("Select Gender", ['Male', 'Female'])]
senior_citizen = senior_citizen_map[st.radio("Is the person a Senior Citizen?", ['Yes', 'No'])]
partner = partner_map[st.radio("Do you have a partner?", ['Yes', 'No'])]
dependents = dependents_map[st.radio("Do you have children or your parents?", ['Yes', 'No'])]
tenure = st.number_input("Enter the number of months you have been using our subscription", min_value=0, max_value=100, value=10)
phone_service = phone_service_map[st.radio("Are you using a phone service?", ['Yes', 'No'])]
multiple_lines = multiple_lines_map[st.radio("Are you using multiple lines?", ['Yes', 'No', 'No phone service'])]
internet_service = internet_service_map[st.radio("Which internet service?", ['DSL', 'Fiber optic', 'No'])]
online_security = online_security_map[st.radio("Do you have antivirus?", ['Yes', 'No', 'No internet service'])]

if online_security != 2:
    device_protection = device_protection_map[st.radio("Do you have any means of Device Protection?", ['Yes', 'No', 'No internet service'])]
    tech_support = tech_support_map[st.radio("Do you have any Tech Support?", ['Yes', 'No', 'No internet service'])]
    streaming_tv = streaming_tv_map[st.radio("Do you Stream on TV?", ['Yes', 'No', 'No internet service'])]
    streaming_movies = streaming_movies_map[st.radio("Do you Stream movies?", ['Yes', 'No', 'No internet service'])]
else:
    device_protection, tech_support, streaming_tv, streaming_movies = [2]*4

contract = contract_map[st.radio("What is the type of service you have?", ['Month-to-month', 'One year', 'Two year'])]
paperless_billing = paperless_billing_map[st.radio("Was it a Paperless Billing?", ['Yes', 'No'])]
payment_method = payment_method_map[st.radio("What was the payment method used?", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])]
monthly_charges = st.number_input("Enter the often monthly charges", min_value=0.0, max_value=10000.0, value=1.5, step=0.01)
total_charges = st.number_input("Enter the often Total Charges", min_value=0.0, max_value=100000.0, value=1.5, step=0.01)

input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior_citizen],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})
prediction=model.predict(input_data)
if prediction[0] == 1:
    st.write("Customer is likely to Churn.")
    gif_sad="https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif?cid=790b7611qyvu91nhsz0jwtkjlkzcd0a3ep1eqfuh5d6d597v&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    st.image(gif_sad,use_column_width=True)

    
else:
    st.write("Customer is unlikely to Churn.")
    gif_hap="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3R1ZTNwY2tkYml4bWdyeGlhaXRmMm9hN2JuYzhvYnZ0eTZ5NzV0diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/G96zgIcQn1L2xpmdxi/giphy.gif"
    st.image(gif_hap,use_column_width=True)
