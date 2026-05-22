# Live-Object-Detection
Real-Time Object Detection and Tracking
Overview
This project is a simple real-time object detection system built using Python, Streamlit, and YOLOv8. It uses your webcam to detect and track objects live on the screen.
Features
•	Real-time object detection 
•	Object tracking using YOLOv8 
•	Live webcam feed 
•	Object count display 
•	Save detected frames 
•	Object alert system 
Requirements
Install the following libraries before running the project:
pip install streamlit
pip install streamlit-webrtc
pip install ultralytics
pip install opencv-python
pip install av
Files Needed
Make sure these files are in the same folder:
•	app.py 
•	yolov8n.pt 
How to Run
Open the terminal and run:
streamlit run app.py
How It Works
1.	The webcam opens in the browser. 
2.	YOLOv8 detects objects from the live video. 
3.	Detected objects are tracked and counted. 
4.	Users can: 
o	Save frames 
o	Set object alerts 
o	View detected object counts 
Technologies Used
•	Python 
•	Streamlit 
•	YOLOv8 
•	OpenCV 
•	WebRTC 
