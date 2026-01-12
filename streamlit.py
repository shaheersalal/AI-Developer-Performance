import streamlit as st
import pandas as pd
import joblib

model = joblib.load('AI_Developer_Performance.joblib')

st.sidebar.header('Enter user info')

def user_input_features():
    Lines_of_Code = st.sidebar.selectbox("Lines_of_Code", list(range(50, 2000, 50)))
    AI_Usage_Hours = st.sidebar.selectbox("AI_Usage_Hours", list(range(1,24)))
    Cognitive_Load = st.sidebar.selectbox("Cognitive_Load", list(range(20,100)))
    Task_Duration_Hours = st.sidebar.number_input('Task_Duration_Hours')
    Errors = st.sidebar.number_input('Errors')

    data = {
        "Lines_of_Code": [Lines_of_Code],
        "AI_Usage_Hours": [AI_Usage_Hours],
        "Cognitive_Load": [Cognitive_Load],
        "Task_Duration_Hours": [Task_Duration_Hours],
        "Errors": [Errors]}
    
    return pd.DataFrame(data)

input_df = user_input_features()

st.subheader("Selected Input")
st.write(input_df)

if st.button("Predict"):
    pred = model.predict(input_df)[0]

    st.success(f"Predicted Task Success Rate: {pred}")