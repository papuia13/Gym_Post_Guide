import numpy as np
import cv2
import mediapipe as mp

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return angle

def calculate_bicep_curl(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
    # Right side
    right_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                      landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    right_elbow = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].y]
    right_wrist = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].y]
    
    right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
    
    cv2.putText(image, str(right_angle), 
                tuple(np.multiply(right_elbow, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Left side
    left_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].y]
    left_elbow = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].y]
    left_wrist = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].y]
    
    left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
    
    cv2.putText(image, str(left_angle), 
                tuple(np.multiply(left_elbow, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Update counter and stage for right side
    if right_angle > 160:
        right_stage = "down"
    if right_angle < 30 and right_stage == 'down':
        right_stage = "up"
        right_counter += 1
        if right_counter % 12 == 0:
            right_set += 1
            right_counter = 0  # Reset right_counter after a set
    
    # Update counter and stage for left side
    if left_angle > 160:
        left_stage = "down"
    if left_angle < 30 and left_stage == 'down':
        left_stage = "up"
        left_counter += 1
        if left_counter % 12 == 0:
            left_set += 1
            left_counter = 0  # Reset left_counter after a set
    
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set
