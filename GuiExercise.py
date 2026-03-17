import streamlit as st

# QUESTION 1
st.title("Welcome GUI App")
st.write("This is my first graphical interface")

# QUESTION 2
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# QUESTION 3
if st.button("Click Me"):
    st.write("Button clicked!")

# QUESTION 4
num1 = st.number_input("Number 1")
num2 = st.number_input("Number 2")

if st.button("Add Numbers"):
    st.write("Sum:", num1 + num2)

# QUESTION 5
if st.checkbox("Show Greeting"):
    st.write("Have a nice day!")

# QUESTION 6
st.subheader("Mini App")

name2 = st.text_input("Enter your name (Mini App)")
n1 = st.number_input("Number 1 (Mini App)")
n2 = st.number_input("Number 2 (Mini App)")
show = st.checkbox("Show Greeting (Mini App)")

if st.button("Submit"):
    st.write(f"Hello {name2}, the sum is {n1 + n2}")
    if show:
        st.write("Have a nice day!")