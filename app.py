import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2
import time

st.set_page_config(
    page_title="Object Detection System",
    layout="wide"
)

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

st.title("Real-Time Object Detection and Tracking")
st.write("Detect and track objects using your live camera feed.")

st.sidebar.title("Control Panel")

save_frames = st.sidebar.toggle("Save Frames")

alert_object = st.sidebar.text_input(
    "Object Alert",
    placeholder="Enter object name"
)

object_counts = {}

def video_frame_callback(frame):
    global object_counts

    img = frame.to_ndarray(format="bgr24")

    results = model.track(
        img,
        persist=True,
        conf=0.5,
        verbose=False
    )

    processed_frame = results[0].plot()

    object_counts = {}

    if results[0].boxes is not None:

        detected_classes = results[0].boxes.cls.tolist()
        class_names = model.names

        for cls in detected_classes:

            label = class_names[int(cls)]

            object_counts[label] = (
                object_counts.get(label, 0) + 1
            )

            if alert_object and label.lower() == alert_object.lower():

                cv2.rectangle(
                    processed_frame,
                    (20, 20),
                    (240, 80),
                    (0, 0, 255),
                    -1
                )

                cv2.putText(
                    processed_frame,
                    "OBJECT DETECTED",
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2
                )

    if save_frames:

        filename = f"detected_{int(time.time())}.jpg"

        cv2.imwrite(filename, processed_frame)

    return av.VideoFrame.from_ndarray(
        processed_frame,
        format="bgr24"
    )

st.subheader("Live Camera Feed")

webrtc_streamer(
    key="live-detection",
    video_frame_callback=video_frame_callback,
    async_processing=True,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False
    },
)

st.subheader("Detected Objects")

if object_counts:

    for obj, count in object_counts.items():
        st.write(f"{obj}: {count}")

else:
    st.info("No objects detected yet.")