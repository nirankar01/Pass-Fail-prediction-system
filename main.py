import streamlit as st
import numpy as np
import joblib
model=joblib.load("model.pkl") #load the trained model from the file

st.title("Pass/Fail Prediction System")
st.write("Enter the marks to predict whether the student will pass or fail.")

hours=st.number_input("Enter the marks obtained by the student:",min_value=0.0,max_value=20.0,step=0.1)

if st.button("Predict"):
    prediction=model.predict([[hours]])
    if(prediction[0]==0):
        st.error("The Student will fail.")
    else:
        st.success("The Student will pass.")
