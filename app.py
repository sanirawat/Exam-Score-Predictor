import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Exam Score Predictor", layout="centered")

st.title("🎓 Student Exam Score Prediction")
st.write("Enter details to predict the exam score")

hours = st.number_input(
    "📘 Hours Studied",
    min_value=0.0,
    step=0.5
)

prev_score = st.number_input(
    "📝 Previous Score",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

attendance = st.number_input("attendance percentage", min_value=0.0,max_value=100.0,step=1.0)

if st.button("Predict Score"):
    input_data = np.array([[hours, prev_score,attendance]])
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Exam Score: **{prediction[0]:.2f}**")
