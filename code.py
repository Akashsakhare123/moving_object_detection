# import libraries
import cv2

# Create background subtractor object
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Open video capture
video_capture = cv2.VideoCapture(0)  # You can replace 0 with the video file path

while True:
    # Read frame from video
    ret, frame = video_capture.read()

    # Apply background subtraction
    foreground_mask = background_subtractor.apply(frame)

    # Perform morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, kernel)

    # Find contours of moving objects
    contours, _ = cv2.findContours(foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding box around moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the area threshold as needed
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Moving Object Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()