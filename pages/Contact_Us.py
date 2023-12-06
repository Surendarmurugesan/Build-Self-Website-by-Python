import streamlit as st
from send_email import send_email

st.title("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Request from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email has sent successfully!!")