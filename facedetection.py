import cv2

# Initialize the cascade classifier with the XML file
faceclassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture video from the default camera using DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Detect faces in the frame
    faces = faceclassifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Display the frame with rectangles drawn around faces
    cv2.imshow('Face Detection', frame)

    # Exit the loop if Esc key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()