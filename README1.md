# 🚄 RailSentinel AI: Autonomous Multi-Agent Edge Ecosystem

**Theme:** Agentic & Autonomous Systems (Railways Track Safety)
**Hackathon:** FAR AWAY 2026 - Round 1 Submission

## ⚠️ The Problem
Modern high-speed trains have braking distances exceeding 1.5 kilometers. Current visual inspections and basic AI camera systems suffer from critical flaws:
1. **Visibility Gaps:** Fog, rain, and night render standard optical cameras useless.
2. **High False Positives:** Basic AI (like YOLO) stops trains for harmless shadows or debris (like plastic bags), costing millions in operational delays.

## 🛡️ Our Novel Solution: VLM + Sensor Fusion
RailSentinel AI introduces an advanced Edge Brain that doesn't just "see"—it **thinks**. 
By fusing simulated 3D LiDAR point clouds with high-speed video, our system creates a sub-millimeter digital twin of the track in real-time. An on-board **Vision-Language Model (VLM)** provides semantic reasoning to eliminate false alarms (e.g., recognizing a shadow lacks physical mass compared to a lethal rock obstruction).

### ⚙️ Technical Architecture
* **Edge AI Core:** Python, OpenCV, Simulated Quantized VLM Inference.
* **Hardware Design:** Custom PCB schematic featuring ESP32-S3, MPU6050 (Vibration IMU), and LoRa Mesh.
* **Operator Dashboard:** Next.js / React / Tailwind CSS for zero-latency cabin telemetry.

## 🚀 Repository Contents
* `/core-ai`: Contains our `vlm_fusion_edge.py` script demonstrating real-time sensor fusion and semantic anomaly reasoning.
* `/dashboard`: Contains the `index.html` frontend for the operator's autonomous hazard alert system.
* *(Hardware PCB schematics and presentations are included in the primary submission portal).*

## 💻 How to Run the AI Demo Locally
1. Ensure Python 3 is installed.
2. Install dependencies: `pip install opencv-python numpy`
3. Run the edge core: `python core-ai/vlm_fusion_edge.py`
