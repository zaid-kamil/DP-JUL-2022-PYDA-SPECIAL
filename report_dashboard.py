# streamlit run report_dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache
def load_report():
    df = pd.read_excel('report1.xlsx')
    df.set_index('Name', inplace=True)
    return df

st.title("Student Marks")
report = load_report()
st.dataframe(report)

names = report.index.tolist()
student = st.selectbox('Select Student', names)

st.subheader(f"selected student: {student}")
student_row = report.loc[student]
st.table(student_row)
fig = px.bar(student_row,
            x=student_row.index,
            y=student)
st.plotly_chart(fig)