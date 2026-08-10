import streamlit as st

st.title("BASIC CALCULATOR")

st.write("### Select an Operation")

choice = st.selectbox(
    "Choose an operation:",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

a = st.number_input("Enter first number:", value=0.0)
b = st.number_input("Enter second number:", value=0.0)

if st.button("Calculate"):

    if choice == "Addition":
        st.success("Addition = " + str(a + b))

    elif choice == "Subtraction":
        st.success("Subtraction = " + str(a - b))

    elif choice == "Multiplication":
        st.success("Multiplication = " + str(a * b))

    elif choice == "Division":
        st.success("Division = " + str(a / b))
