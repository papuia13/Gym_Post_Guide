import numpy as np
import cv2
import mediapipe as mp

#if time permits:for each and every excercise we need to make the prepose function which will initialize the counter, stage and set
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
    if right_angle < 45 and right_stage == 'down':
        right_stage = "up"
        right_counter += 1
        if right_counter % 12 == 0:
            right_set += 1
            right_counter = 0  # Reset right_counter after a set
    
    # Update counter and stage for left side
    if left_angle > 160:
        left_stage = "down"
    if left_angle < 45 and left_stage == 'down':
        left_stage = "up"
        left_counter += 1
        if left_counter % 12 == 0:
            left_set += 1
            left_counter = 0  # Reset left_counter after a set
    
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_tricep_extension(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
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
    if right_angle < 50:
        right_stage = "up"
    if right_angle > 160 and right_stage == 'up':
        right_stage = "down"
        right_counter += 1
        if right_counter % 12 == 0:
            right_set += 1
            right_counter = 0  # Reset right_counter after a set
            
    if left_angle < 50:
        left_stage = "up"
    if left_angle > 160 and left_stage == 'up':
        left_stage = "down"
        left_counter += 1
        if left_counter % 12 == 0:
            left_set += 1
            left_counter = 0  # Reset left_counter after a set
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_shoulder_press(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
    # Right side
    right_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                      landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    right_elbow = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].y]
    right_wrist = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].y]
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    
    right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
    right_shoulder_angle = calculate_angle(right_hip, right_shoulder, right_elbow)
    
    cv2.putText(image, str(right_shoulder_angle), 
                tuple(np.multiply(right_shoulder, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    # Left side
    left_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].y]
    left_elbow = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].y]
    left_wrist = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].y]
    left_hip = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y]
    
    left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
    left_shoulder_angle = calculate_angle(left_hip, left_shoulder, left_elbow)
    
    cv2.putText(image, str(left_shoulder_angle), 
                tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Update counter and stage for right side
    if right_shoulder_angle < 70 and right_elbow_angle < 70:
        right_stage = "down"
    if right_shoulder_angle > 160 and right_elbow_angle > 160 and right_stage == 'down':
        right_stage = "up"
        right_counter += 1
        if right_counter % 12 == 0:
            right_set += 1
            right_counter = 0  # Reset right_counter after a set

    if left_shoulder_angle < 70 and left_elbow_angle < 70:
        left_stage = "down"
    if left_shoulder_angle > 160 and left_elbow_angle > 160 and left_stage == 'down':
        left_stage = "up"
        left_counter += 1
        if left_counter % 12 == 0:
            left_set += 1
            left_counter = 0  # Reset left_counter after a set
            
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_crunches(landmarks, image, counter, stage, sets):
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
        stage = "down"
    if right_angle < 30 and stage == 'down':
        stage = "up"
        counter += 1
        if counter % 12 == 0:
            sets += 1
            counter = 0  # Reset counter after a set
    return counter, stage, sets

def calculate_leg_raise(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
    # Right side
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    right_ankle = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    right_angle = calculate_angle(right_hip, right_knee, right_ankle)
    
    cv2.putText(image, str(right_angle), 
                tuple(np.multiply(right_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Left side
    left_hip = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y]
    left_knee = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y]
    left_ankle = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].y]
    
    left_angle = calculate_angle(left_hip, left_knee, left_ankle)
    
    cv2.putText(image, str(left_angle), 
                tuple(np.multiply(left_knee, [640, 480]).astype(int)), 
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
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_leg_curl(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
    # Right side
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    right_ankle = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    right_angle = calculate_angle(right_hip, right_knee, right_ankle)
    
    cv2.putText(image, str(right_angle), 
                tuple(np.multiply(right_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Left side
    left_hip = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y]
    left_knee = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y]
    left_ankle = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].y]
    
    left_angle = calculate_angle(left_hip, left_knee, left_ankle)
    
    cv2.putText(image, str(left_angle), 
                tuple(np.multiply(left_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Update counter and stage for right side
    if right_angle > 160:
        right_stage = "down"
    if right_angle < 30 and right_stage == 'down':
        right_stage = "up"
        right_counter += 1
        if right_counter % 12 == 0:
            right_set += 1
            right_counter = 0
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_bench_press(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
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
            right_counter = 0
            
    if left_angle > 160:
        left_stage = "down"
    if left_angle < 30 and left_stage == 'down':
        left_stage = "up"
        left_counter += 1
        if left_counter % 12 == 0:
            left_set += 1
            left_counter = 0
    return right_counter, left_counter, right_stage, left_stage, right_set, left_set

def calculate_pullup(landmarks, image, right_counter, left_counter, right_stage, left_stage, right_set, left_set):
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

def calculate_squat(landmarks, image, counter, stage, sets):
    # Right side
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    right_ankle = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    right_angle = calculate_angle(right_hip, right_knee, right_ankle)
    
    cv2.putText(image, str(right_angle), 
                tuple(np.multiply(right_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Left side
    left_hip = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y]
    left_knee = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y]
    left_ankle = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].y]
    
    left_angle = calculate_angle(left_hip, left_knee, left_ankle)
    
    cv2.putText(image, str(left_angle), 
                tuple(np.multiply(left_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Update counter and stage for right side
    if right_angle > 160:
        stage = "down"
    if right_angle < 30 and stage == 'down':
        stage = "up"
        counter += 1
        if counter % 12 == 0:
            sets += 1
            counter = 0  # Reset counter after a set
            
    return counter, stage, sets

def calculate_pushup(landmarks, image, counter, stage, sets):
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
        stage = "down"
    if right_angle < 30 and stage == 'down':
        stage = "up"
        counter += 1
        if counter % 12 == 0:
            sets += 1
            counter = 0  # Reset counter after a set
    return counter, stage, sets

def calculate_deadlift(landmarks, image, counter, stage, sets):
    # Right side
    right_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                      landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    right_ankle = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    right_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)
    right_hip_angle = calculate_angle(right_shoulder, right_hip, right_knee)
    
    cv2.putText(image, str(right_knee_angle), 
                tuple(np.multiply(right_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, str(right_hip_angle),
                tuple(np.multiply(right_hip, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # Update counter and stage for right side
    if right_knee_angle < 150 and right_hip_angle < 55:
        stage = "down"
    if (right_knee_angle > 160 and right_hip_angle > 160) and stage == 'down':
        stage = "up"
        counter += 1
        if counter % 12 == 0:
            sets += 1
            counter = 0  # Reset counter after a set
    return counter, stage, sets

def calculate_lunges(landmarks, image, counter, stage, sets):
    # Right side
    right_hip = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    right_ankle = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    right_angle = calculate_angle(right_hip, right_knee, right_ankle)
    
    cv2.putText(image, str(right_angle), 
                tuple(np.multiply(right_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Left side
    left_hip = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y]
    left_knee = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x,
                 landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y]
    left_ankle = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].x,
                  landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].y]
    
    left_angle = calculate_angle(left_hip, left_knee, left_ankle)
    
    cv2.putText(image, str(left_angle), 
                tuple(np.multiply(left_knee, [640, 480]).astype(int)), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Update counter and stage for right side
    if right_angle > 160:
        stage = "down"
    if right_angle < 30 and stage == 'down':
        stage = "up"
        counter += 1
        if counter % 12 == 0:
            sets += 1
            counter = 0  # Reset counter after a set
    return counter, stage, sets

def calculate_plank(landmarks, image, start_time, sets, duration=20):
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
    
    # Calculate duration
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    if elapsed_time >= duration:
        sets += 1
        start_time = cv2.getTickCount()  # Reset start time for the next set
    
    cv2.putText(image, f'Time: {int(elapsed_time)}s', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, f'Sets: {sets}', (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    return start_time, sets


