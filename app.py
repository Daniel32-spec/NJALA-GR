import streamlit as st
import pandas as pd
import joblib
import os
from docx import Document

st.title("Njala Grade Point Predictor")

# Debug: list directory contents
st.write("Files in working directory:", os.listdir("."))

# Load model
model = joblib.load("model.joblib")

# Input fields
st.sidebar.header("Student Information")
insert = st.sidebar.number_input("Insert Grade", min_value=0, max_value=100, step=1)
credit = st.sidebar.number_input("Credit Hour", min_value=0.0, max_value=10.0, step=0.5, format="%.1f")

# Prediction
if st.sidebar.button("Predict"):
    # Model expects 2 features: [insert, credit]
    prediction = model.predict([[insert, credit]])
    result = "Pass" if prediction[0] == 1 else "Fail"
    st.write(f"Prediction: **{result}**")
