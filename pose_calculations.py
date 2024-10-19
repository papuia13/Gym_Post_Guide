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

def calculate_bicep_curl(landmarks, image, counter, stage):
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
    
    return counter, stage

def calculate_tricep_extension(landmarks, image, counter, stage):
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
    
    if angle < 30:
        stage = "down"
    if angle > 160 and stage == 'down':
        stage = "up"
        counter += 1
    
    return counter, stage

def calculate_shoulder_press(landmarks, image, counter, stage):
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
    
    return counter, stage