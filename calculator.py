import streamlit as st
st.title("hello SRU")
print("==============================")
print("      BASIC CALCULATOR")
print("==============================")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Addition =", a + b)

elif choice == 2:
    print("Subtraction =", a - b)

elif choice == 3:
    print("Multiplication =", a * b)

elif choice == 4:
    print("Division =", a / b)

else:
    print("Invalid choice")
