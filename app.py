import streamlit as st

st.title("subtaction Program")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("sub"):
    result = num1 - num2
    st.success(f"subtraction = {result}")
