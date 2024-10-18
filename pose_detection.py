import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image

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

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return angle

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
        
        shoulder = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                    landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].y]
        
        angle = calculate_angle(shoulder, elbow, wrist)
        
        cv2.putText(image, str(angle), 
                    tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        
        if angle > 160:
            stage = "down"
        if angle < 30 and stage == 'down':
            stage = "up"
            counter += 1
        
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

