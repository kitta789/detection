import streamlit as st
import cv2
from PIL import Image
import numpy as np

def get_available_cameras():
    """Get a list of available camera indices."""
    camera_indices = []
    for i in range(10):  # Check first 10 indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_indices.append(i)
            cap.release()
    return camera_indices

def main():
    st.title("Camera Selection and Capture App")

    # Get available cameras
    camera_indices = get_available_cameras()
    
    if not camera_indices:
        st.error("No cameras found. Please connect a camera and try again.")
        return

    # Camera selection
    selected_camera = st.selectbox("Select Camera", camera_indices)

    # Camera capture
    image = st.camera_input("Take a picture", key=f"camera_{selected_camera}")

    if image is not None:
        # Display the captured image
        st.image(image, caption="Captured Image", use_column_width=True)

        # Add a download button for the captured image
        st.download_button(
            label="Download Image",
            data=image.getvalue(),
            file_name="captured_image.jpg",
            mime="image/jpeg"
        )

if __name__ == "__main__":
    main()