import streamlit as st

st.title("Demo Streamlit")
st.write("Hello! Welcome to Beginner Website Using Streamlit")

name = st.text_input("Your Name:")
if st.button("Submit"):
   st.success(f"Hai {name}! Welcome to this Beginner Website")
