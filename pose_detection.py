import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image
from pose_calculations import calculate_bicep_curl, calculate_tricep_extension, calculate_shoulder_press

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
counter = 0
stage = None

stframe = st.empty()
st.sidebar.text("Reps Counter")
reps_counter = st.sidebar.empty()

stop_button = st.sidebar.button('Stop')
bicep_button = st.sidebar.button('Bicep Curl')
tricep_button = st.sidebar.button('Tricep Extension')
shoulder_button = st.sidebar.button('Shoulder Press')

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
            counter, stage = calculate_bicep_curl(landmarks, image, counter, stage)
        if tricep_button:
            counter, stage = calculate_tricep_extension(landmarks, image, counter, stage)
        if shoulder_button:
            counter, stage = calculate_shoulder_press(landmarks, image, counter, stage)
        
    except:
        pass
    
    mp.solutions.drawing_utils.draw_landmarks(image, result.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS,
                                              mp.solutions.drawing_utils.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                              mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
    
    stframe.image(image, channels='BGR')
    reps_counter.text(f"Reps: {counter}")
    
    if stop_button:
        break

cap.release()
cv2.destroyAllWindows()