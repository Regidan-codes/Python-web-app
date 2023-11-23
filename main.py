import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Abhishek N")
    content = """
    Hi, I'm Abhishek N,I'm a python programmer and data science enthusiast. I've worked on various software technologies
    like JAVA and C. I'm creating python projects to enhance my portfolio. I've also been learning and implementing 
    various machine learning projects, do checkout my github profile.
    """
    st.info(content)

content2 = """
Below are some of the apps I've built in python. Feel free to contact me for more info.
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
