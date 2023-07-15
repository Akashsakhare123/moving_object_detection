# import libraries
import cv2

# Create background subtractor object
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Open video capture
video_capture = cv2.VideoCapture(0)  # You can replace 0 with the video file path