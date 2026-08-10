import streamlit as st
st.title("BASIC CALCULATOR")
st.title("1. Addition")
st.title("2. Subtraction")
st.title("3. Multiplication")
st.title("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    st.title("Addition =", a + b)

elif choice == 2:
    st.title("Subtraction =", a - b)

elif choice == 3:
    st.title("Multiplication =", a * b)

elif choice == 4:
    st.title("Division =", a / b)

else:
    st.title("Invalid choice")
