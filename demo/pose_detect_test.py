import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image
from pose_cal_test import calculate_bicep_curl

st.title("Pose Detection using mediapipe")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;   
    }
    .css-1v3fvcr {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Settings")
st.sidebar.subheader("Choose the model")

@st.cache_resource
def load_model():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    return pose

pose = load_model()

cap = cv2.VideoCapture(0)
'''counter = 0
stage = None
sets = 0
'''
left_counter = 0
right_counter = 0
left_stage = None
right_stage = None
left_set = 0
right_set = 0

stframe = st.empty()
st.sidebar.text("Reps Counter")
'''reps_counter = st.sidebar.empty()
sets_counter = st.sidebar.empty()'''
right_sets_counter = st.sidebar.empty()
left_sets_counter = st.sidebar.empty()
right_reps_counter = st.sidebar.empty()
left_reps_counter = st.sidebar.empty()

stop_button = st.sidebar.button('Stop')
bicep_button = st.sidebar.button('Bicep Curl')


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    result = pose.process(image)
    
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    try:
        landmarks = result.pose_landmarks.landmark
        
        if bicep_button:
            right_counter, left_counter, right_stage, left_stage, right_set, left_set = calculate_bicep_curl(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set)   
       
    except:
        pass
    
    mp.solutions.drawing_utils.draw_landmarks(image, result.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS,
    mp.solutions.drawing_utils.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
    mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
    
    stframe.image(image, channels='BGR')
    '''reps_counter.text(f"Reps: {counter}")
    sets_counter.text(f"Sets: {sets}")'''
    
    right_reps_counter.text(f"Right Reps: {right_counter}")
    left_reps_counter.text(f"Left Reps: {left_counter}")
    right_sets_counter.text(f"Right Sets: {right_set}")
    left_sets_counter.text(f"Left Sets: {left_set}")
    
    if stop_button:
        break

cap.release()
cv2.destroyAllWindows()