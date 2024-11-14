import streamlit as st
from pose_detection import pose_detection
from string_routenes import NutritionTbl_Ls18, NutritionTbl_bt18n24, NutritionTbl_bt25n29, NutritionTbl_gt30, WorkoutTbl_Ls18, WorkoutTbl_bt18n24, WorkoutTbl_bt25n29, WorkoutTbl_gt30

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
        return NutritionTbl_Ls18
    elif 18.5 <= bmi < 24.9:
        return NutritionTbl_bt18n24
    elif 25 <= bmi < 29.9:
        return NutritionTbl_bt25n29
    else:
        return NutritionTbl_gt30

def get_workout_plan(bmi):
    if bmi < 18.5:
        return WorkoutTbl_Ls18
    elif 18.5 <= bmi < 24.9:
        return WorkoutTbl_bt18n24
    elif 25 <= bmi < 29.9:
        return WorkoutTbl_bt25n29
    else:
        return WorkoutTbl_gt30

# Set page configuration
st.set_page_config(page_title="Gym Action Tracker", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for aesthetic UI/UX
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #f0f2f6, #e6e6e6);
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #e6e6e6;
        color: #333;
    }
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #4b47cc;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "BMI Calculator", "Nutrition Plan", "Workout Plan", "Pose Detection"])

# Page title and description
st.markdown("# 🏋️ Gym Action Tracker")
st.markdown("Welcome to the **Gym Action Tracker**! This web application helps you track your gym actions and provides personalized fitness and nutrition plans.")

if page == "Home":
    st.markdown("## 🚀 Get Started")
    st.markdown("Hit the gym and start your fitness journey today!")
    
    st.markdown("### Features")
    st.markdown("""
            - **Body Mass Index (BMI) Calculator**: Calculate your BMI to know if you are underweight, normal, overweight, or obese.
            - **Nutrition Plan**: Get a personalized nutrition plan based on your BMI to help you achieve your fitness goals.
            - **Workout Plan**: Receive a customized workout plan tailored to your BMI and fitness level.
            - **Pose Detection**: Use pose detection to ensure you are performing exercises correctly and safely.
            """)

    st.markdown("### How to Use")
    st.markdown("""
            1. **Calculate Your BMI**: Go to the BMI Calculator page and enter your weight and height to calculate your BMI.
            2. **Get Your Nutrition Plan**: After calculating your BMI, go to the Nutrition Plan page to receive a personalized nutrition plan.
            3. **Get Your Workout Plan**: Similarly, go to the Workout Plan page to get a customized workout plan based on your BMI.
            4. **Use Pose Detection**: Navigate to the Pose Detection page to start the pose detection feature and ensure you are performing exercises correctly.
            """)

    st.markdown("### About Us")
    st.markdown("""
            The Gym Action Tracker is designed to help you achieve your fitness goals by providing personalized fitness and nutrition plans. Whether you are a beginner or an experienced gym-goer, our application offers tools and resources to support your fitness journey.
            """)

    st.markdown("### Contact Us")
    st.markdown("""
            For any inquiries or support, please contact us at [support@gymtracker.com](mailto:support@gymtracker.com).
            """)


elif page == "BMI Calculator":
    st.markdown("## 📏 Body Mass Index")
    st.markdown("Calculate your BMI to know if you are underweight, normal, overweight, or obese.")

    with st.form(key='bmi_form'):
        weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
        height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1)
        submit_button = st.form_submit_button(label='Calculate BMI')
        
        if submit_button:
            bmi_result, bmi_value = calculate_bmi(weight, height)
            st.write(bmi_result)
            if bmi_value:
                st.session_state.bmi_value = bmi_value

elif page == "Nutrition Plan":
    st.markdown("## 🍎 Nutrition")
    st.markdown("Get the best nutrition plan tailored for your body.")

    if st.button("Get Nutrition Plan"):
        if 'bmi_value' in st.session_state:
            nutrition_plan = get_nutrition_plan(st.session_state.bmi_value)
            st.write(nutrition_plan)
        else:
            st.write("Please calculate your BMI first.")

elif page == "Workout Plan":
    st.markdown("## 🏃 Workout Plan")
    st.markdown("Get a personalized workout plan based on your BMI.")

    if st.button("Get Workout Plan"):
        if 'bmi_value' in st.session_state:
            workout_plan = get_workout_plan(st.session_state.bmi_value)
            st.write(workout_plan)
        else:
            st.write("Please calculate your BMI first.")

elif page == "Pose Detection":
    st.markdown("## 📸 Pose Detection")
    st.markdown("Start or stop the pose detection feature.")

    if 'pose_detection_running' not in st.session_state:
        st.session_state.pose_detection_running = False

    if st.button("Start Pose Detection"):
        st.session_state.pose_detection_running = True

    if st.session_state.pose_detection_running:
        if st.button("Stop Pose Detection"):
            st.session_state.pose_detection_running = False
        pose_detection()

# Footer
st.markdown("---")
st.markdown("### 📧 Contact Us")
st.markdown("For any inquiries, please contact us at [support@gymtracker.com](mailto:support@gymtracker.com).")
