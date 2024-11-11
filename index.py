import streamlit as st
import mediapipe as mp
import cv2
from pose_calculations import calculate_bicep_curl, calculate_tricep_extension, calculate_shoulder_press, calculate_deadlift, calculate_squat, calculate_plank
from pose_detection import pose_detection

def calculate_bmi(weight, height):
    try:
        if height > 0:
            bmi = weight / ((height / 100) ** 2)
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
            return f"Your BMI is: {bmi:.2f} ({category})", bmi
        else:
            return "Please enter a valid height.", None
    except Exception as e:
        return f"Error in BMI calculation: {e}", None

def get_nutrition_plan(bmi):
    if bmi < 18.5:
        return "You are underweight. Consider a diet rich in proteins, healthy fats, and carbohydrates."
    elif 18.5 <= bmi < 24.9:
        return "You have a normal weight. Maintain a balanced diet with a mix of proteins, fats, and carbohydrates."
    elif 25 <= bmi < 29.9:
        return "You are overweight. Focus on a diet with more proteins and vegetables, and fewer carbohydrates."
    else:
        return "You are obese. Consult a nutritionist for a personalized diet plan."

def get_workout_plan(bmi):
    if bmi < 18.5:
        return "Focus on strength training exercises to build muscle mass."
    elif 18.5 <= bmi < 24.9:
        return "Maintain a balanced workout routine with a mix of cardio and strength training."
    elif 25 <= bmi < 29.9:
        return "Incorporate more cardio exercises to help with weight loss."
    else:
        return "Consult a fitness trainer for a personalized workout plan."

# Set page configuration
st.set_page_config(page_title="Gym Action Tracker", layout="wide")

# Page title and description
st.markdown("# 🏋️ Gym Action Tracker")
st.markdown("Welcome to the **Gym Action Tracker**! This web application helps you track your gym actions and provides personalized fitness and nutrition plans.")

# Create columns with adjusted widths
col1, col2, col3, col4, col5 = st.columns([2, 0.1, 2, 0.1, 2])

# Body Mass Index section
col1.markdown("## 📏 Body Mass Index")
col1.markdown("Calculate your BMI to know if you are underweight, normal, overweight, or obese.")

with col1.form(key='bmi_form'):
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1)
    submit_button = st.form_submit_button(label='Calculate BMI')
    
    if submit_button:
        bmi_result, bmi_value = calculate_bmi(weight, height)
        col1.write(bmi_result)
        if bmi_value:
            st.session_state.bmi_value = bmi_value

# Empty column for spacing
col2.markdown("")

# Nutrition section
col3.markdown("## 🍎 Nutrition")
col3.markdown("Get the best nutrition plan tailored for your body.")

if col3.button("Get Nutrition Plan"):
    if 'bmi_value' in st.session_state:
        nutrition_plan = get_nutrition_plan(st.session_state.bmi_value)
        col3.write(nutrition_plan)
    else:
        col3.write("Please calculate your BMI first.")

# Empty column for spacing
col4.markdown("")

# Get Started section
col5.markdown("## 🚀 Get Started")
col5.markdown("Hit the gym and start your fitness journey today!")
col5.markdown(
    """
    <style>
    .stButton>button {
        background-color: #aba1e7;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'pose_detection_running' not in st.session_state:
    st.session_state.pose_detection_running = False

if col5.button("Start"):
    st.session_state.pose_detection_running = True

if st.session_state.pose_detection_running:
    if col5.button("Stop Pose Detection"):
        st.session_state.pose_detection_running = False
    pose_detection()

# Footer
st.markdown("---")
st.markdown("### 📧 Contact Us")
st.markdown("For any inquiries, please contact us at [support@gymtracker.com](mailto:support@gymtracker.com).")

# Workout Plan section
col3.markdown("## 🏃 Workout Plan")
col3.markdown("Get a personalized workout plan based on your BMI.")

if col3.button("Get Workout Plan"):
    if 'bmi_value' in st.session_state:
        workout_plan = get_workout_plan(st.session_state.bmi_value)
        col3.write(workout_plan)
    else:
        col3.write("Please calculate your BMI first.")
