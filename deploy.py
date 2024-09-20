import streamlit as st
import joblib
loaded_model=joblib.load('logistic_regression_model.pkl')
print(loaded_model)
st.title("logistic regression")