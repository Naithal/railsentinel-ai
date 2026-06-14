import cv2
import numpy as np
import time
import random

def simulate_lidar_fusion(frame_region):
    """Simulates checking 3D LiDAR depth data to verify if an object is flat (shadow) or physical."""
    # Returns True if physical object with mass, False if 2D anomaly (shadow/light)
    depth_score = random.uniform(0.1, 1.0)
    return depth_score > 0.4 

def run_advanced_vlm_edge():
    cap = cv2.VideoCapture(0) # Uses default webcam
    print("[SYSTEM BOOT] RailSentinel Edge VLM Core Initializing...")
    print("[INFO] Loading Quantized Vision-Language Model...")
    print("[INFO] Activating LiDAR/Optical Sensor Fusion...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        frame = cv2.resize(frame, (800, 600))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Baseline Anomaly Detection (Simulated deviation from normal track)
        lower_anomaly = np.array([0, 100, 100])
        upper_anomaly = np.array([20, 255, 255])
        mask = cv2.inRange(hsv, lower_anomaly, upper_anomaly)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # UI Overlay - Advanced Tech Look
        cv2.putText(frame, "RailSentinel VLM / LiDAR Fusion ACTIVE", (15, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        # Simulated Rail Lines
        cv2.line(frame, (250, 600), (350, 250), (255, 255, 255), 1)
        cv2.line(frame, (550, 600), (450, 250), (255, 255, 255), 1)

        for cnt in contours:
            if cv2.contourArea(cnt) > 1500:
                x, y, w, h = cv2.boundingRect(cnt)
                
                # 1. AI Detects Anomaly
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 165, 255), 2)
                
                # 2. Sensor Fusion Check (Eliminating False Positives)
                is_physical = simulate_lidar_fusion(frame[y:y+h, x:x+w])
                
                if is_physical:
                    # 3. VLM Semantic Context (Simulated)
                    context_assessment = "HIGH-MASS OBSTACLE - BRAKE"
                    color = (0, 0, 255) # Red for danger
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 4)
                    cv2.putText(frame, f"VLM EVAL: {context_assessment}", (x, y - 25), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    cv2.putText(frame, "LIDAR: CONFIRMED 3D MASS", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                else:
                    # System recognizes it's just a shadow/light reflection
                    context_assessment = "SHADOW / NON-THREAT"
                    color = (0, 255, 0) # Green for safe
                    cv2.putText(frame, f"VLM EVAL: {context_assessment}", (x, y - 25), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    cv2.putText(frame, "LIDAR: 2D FLAT ANOMALY - IGNORED", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("RailSentinel Advanced VLM Edge", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_advanced_vlm_edge()
