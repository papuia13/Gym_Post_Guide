import streamlit as st

def main():
    st.title("Body Mass Index (BMI) Calculator")

    weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.write(f"Your BMI is {bmi:.2f}")
        else:
            st.warning("Height must be greater than 0")

if __name__ == '__main__':
    main()