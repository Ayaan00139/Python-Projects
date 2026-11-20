import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2 
import mediapipe as mp
from collections import deque
import numpy as np

alarm=False

hip_history = deque(maxlen=15) # Global 
result_history =deque(maxlen=15)
display_window=[]
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def draw_dashboard(frame, result, alarm):
    frame_h, frame_w = frame.shape[:2]
    dash_h = 380
    dashboard = np.zeros((dash_h, frame_w, 3), dtype=np.uint8)
    cv2.line(dashboard, (0, 0), (frame_w, 0), (60, 60, 60), 2)
    cv2.putText(dashboard, "SYSTEM: ACTIVE MONITORING", (25, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (140, 140, 140), 1)
    cards = [
        ("Possible Fall", "POSSIBLE FALL · REVIEW"),
        ("SITTING", "SITTING"),
        ("STANDING", "STANDING"),
        ("Cant See Full Body", "CAN'T SEE FULL BODY"),
        ("No Person","NO PERSON"),
        ("LYING DOWN","LYING DOWN")
    ]
    
    card_y = 50
    card_w = frame_w - 50
    card_h = 42

    for key, label in cards:
        is_active = (result == key)

        if key == "Possible Fall" and (is_active or alarm):
            bg_color = (0, 0, 220)      # Flashing Emergency RED
            text_color = (255, 255, 255)
        elif is_active:
            bg_color = (240, 240, 240)  # Active = Sleek White Card
            text_color = (20, 20, 20)
        else:
            bg_color = (20, 20, 20)     # Inactive = Deep Dark Gray
            text_color = (90, 90, 90)

        cv2.rectangle(dashboard, (25, card_y), (25 + card_w, card_y + card_h), bg_color, -1)
        cv2.rectangle(dashboard, (25, card_y), (25 + card_w, card_y + card_h), (50, 50, 50), 1)
        cv2.putText(dashboard, label, (45, card_y + 28), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, text_color, 2)
        card_y += 55

    return np.vstack([frame, dashboard])

def open_camera():
    global display_window
    global alarm
    cam=cv2.VideoCapture(0)
    while cam.isOpened():
        success,frame=cam.read()
        if not success:
            continue # will continue from the top of the loop

        frame=cv2.flip(frame,1)
        # Convert BGR (OpenCV format) to RGB (MediaPipe format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if not results:
            continue # will continue from the top of the loop
        if not results.pose_landmarks:
            result="No Person"
        else:
            lm = results.pose_landmarks.landmark
            shoulder_y = (lm[11].y + lm[12].y) / 2  # Average height of the two shoulders
            shoulder_x = (lm[11].x + lm[12].x) / 2

            hip_y = (lm[23].y + lm[24].y) / 2 # Average height of the two hips
            hip_x = (lm[23].x + lm[24].x) / 2

            knee_y = (lm[25].y + lm[26].y) / 2 # Average height of the knees
            knee_visibility = (lm[25].visibility+lm[26].visibility) / 2 
            hip_visibility = (lm[23].visibility+lm[24].visibility) / 2 # Visibility Of Hips
            shoulder_visibility = (lm[11].visibility+lm[12].visibility) / 2 # Visibility Of Shoulders
            hip_history.append(hip_y)
            # print(shoulder_x,shoulder_y,hip_x,hip_y,knee_y) 
            alarm,result=calculate(shoulder_x,shoulder_y,hip_x,hip_y,knee_y,knee_visibility,hip_visibility,shoulder_visibility)
            if alarm:
                result="Possible Fall"
            
        display_window = draw_dashboard(frame, result, alarm)
        cv2.imshow("Fall Detector", display_window) # shows frame in window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

def calculate(shoulder_x,shoulder_y,hip_x,hip_y,knee_y,knee_visibility,hip_visibility,shoulder_visibility):
    
    global hip_history
    global last_fall_time
    global alarm
    if hip_visibility<0.5 or shoulder_visibility<0.5:
        return alarm,"Cant See Full Body"

    vertical_spine = abs(hip_y - shoulder_y)
    horizontal_spine = abs(hip_x - shoulder_x)
    thigh_height = knee_y - hip_y
    torso_height = hip_y - shoulder_y
    ratio = thigh_height / (torso_height+0.0001) # +0.0001 avoids zero division
    status = "CALIBRATING..."

    if len(hip_history)==15:
        gap=hip_y - hip_history[0]
        if gap>0.35 :
            status="Possible Fall"
            alarm=True
        else:
            if horizontal_spine > vertical_spine or vertical_spine < 0.15:
                status = "LYING DOWN"
            elif ratio < 0.55:
                status = "SITTING"
                alarm=False
            elif ratio>=0.55:
                status = "STANDING"
                alarm=False
    return alarm,status


def main():
    open_camera()

if __name__=="__main__":
    main()
        

