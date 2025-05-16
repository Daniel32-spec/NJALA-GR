import streamlit as st
import pandas as pd
import joblib
from docx import Document

st.title("Njala Grade Point Predictor")

# Load model
model = joblib.load("model.joblib")

# Input fields
st.sidebar.header("Student Information")
insert = st.sidebar.number_input("Insert Grade", min_value=0, max_value=100, step=1)
credit = st.sidebar.number_input("Credit Hour", min_value=0.0, step=0.5)

# Prediction
if st.sidebar.button("Predict"):
    prediction = model.predict([[insert, credit]])
    result = "Pass" if prediction[0] == 1 else "Fail"
    st.write(f"Prediction: **{result}**")
