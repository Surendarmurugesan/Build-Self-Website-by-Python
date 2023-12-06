# Install streamlit module for website.
import streamlit as st
import pandas

st.set_page_config(layout="wide")
# columns is method.
col1, col2 = st.columns(2)

with col1:
    st.image("./images/photo.png", width=500)

with col2:
    st.title("Surendar Murugesan")
    content = """
    Hello, 
    I'm working as a DevOps professional, totally 5 years accomplished experience in Multi-cloud Administration, Container Orchestration, Infrastructure, Automation, CI/CD, Monitoring and Architecting cloud 
    solutions. I have worked on various tools like AWS, Terraform, Kubernetes, Docker, Jenkins, Python & so on.
    """
    st.info(content)

performed_skil = """ Below you can find some of the apps I have built in Python. Feel free to contact me !!"""
st.write(performed_skil)

col3, empty_col, col4 = st.columns([2, 0.1, 2])

df = pandas.read_csv("data.csv", sep= ";")

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        st.write(f"[Source code]({rows['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        st.write(f"[Source code]({rows['url']})")