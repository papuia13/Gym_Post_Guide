import streamlit as st
import mediapipe as mp
import cv2
from pose_calculations import calculate_bicep_curl, calculate_tricep_extension, calculate_shoulder_press, calculate_deadlift, calculate_squat, calculate_plank

st.title("Pose Detection")
st.write("Please Stand 3 meters away from the camera for better results")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;  /* Reduced width */
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;  /* Reduced width */
        margin-left: -250px;   
    }
    .css-1v3fvcr {
        width: 100%;
    }
    [data-testid="stImage"] {
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Choose the model")
st.sidebar.subheader("Status")

@st.cache_resource
def load_model():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    return pose

pose = load_model()

cap = cv2.VideoCapture(0)
counter = 0
stage = None
sets = 0

left_counter = 0
right_counter = 0
left_stage = None
right_stage = None
left_set = 0
right_set = 0

stframe = st.empty()
#st.sidebar.text("Status : ")
sets_counter = st.sidebar.empty()
reps_counter = st.sidebar.empty()
right_sets_counter = st.sidebar.empty()
left_sets_counter = st.sidebar.empty()
right_reps_counter = st.sidebar.empty()
left_reps_counter = st.sidebar.empty()

bicep_button = st.sidebar.button('Bicep Curl')
tricep_button = st.sidebar.button('Tricep')
shoulder_button = st.sidebar.button('Shoulder Press')
deaflift_button = st.sidebar.button('Deadlift')
stop_button = st.sidebar.button('Stop')

current_exercise=None

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
            if current_exercise != 'bicep':
                # Reset counters when switching to bicep
                right_counter = 0
                left_counter = 0
                right_stage = None
                left_stage = None
                right_set = 0
                left_set = 0
                current_exercise = 'bicep'
            right_counter, left_counter, right_stage, left_stage, right_set, left_set = calculate_bicep_curl(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set)
        
        elif tricep_button:
            if current_exercise != 'tricep':
                # Reset counters when switching to tricep
                right_counter = 0
                left_counter = 0
                right_stage = None
                left_stage = None
                right_set = 0
                left_set = 0
                current_exercise = 'tricep'
            right_counter, left_counter, right_stage, left_stage, right_set, left_set = calculate_tricep_extension(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set)
            
        elif shoulder_button:
            if current_exercise != 'shoulder':
                # Reset counters when switching to shoulder
                right_counter = 0
                left_counter = 0
                right_stage = None
                left_stage = None
                right_set = 0
                left_set = 0
                current_exercise = 'shoulder'
            right_counter, left_counter, right_stage, left_stage, right_set, left_set = calculate_shoulder_press(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set)
            
        elif deaflift_button:
            if current_exercise != 'deadlift':
                right_counter = 0
                left_counter = 0
                right_stage = None
                left_stage = None
                right_set = 0
                left_set = 0
                current_exercise = 'deadlift'
            counter, stage, sets = calculate_deadlift(landmarks, image, counter, stage, sets)
            
    except AttributeError as e:
        st.error(f"An error occurred: {e}")
        
    # Displaying the landmarks and connections    
    mp.solutions.drawing_utils.draw_landmarks(image, result.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS,
    mp.solutions.drawing_utils.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
    mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
    
    # Displaying the main Camera feed    
    stframe.image(image, channels='BGR', use_column_width=False, width=900)
    
    # Status Outputs
    right_reps_counter.text(f"Right Reps: {right_counter}")
    left_reps_counter.text(f"Left Reps: {left_counter}")
    right_sets_counter.text(f"Right Sets: {right_set}")
    left_sets_counter.text(f"Left Sets: {left_set}")  
    reps_counter.text(f"Reps: {counter}")
    sets_counter.text(f"Sets: {sets}")
            
    if stop_button:
        break

cap.release()
cv2.destroyAllWindows()