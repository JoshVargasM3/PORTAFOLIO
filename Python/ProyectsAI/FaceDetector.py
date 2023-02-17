import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            
    for face in faces:
        shape = predictor(gray, face)
        for i in range(0, 16):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        for i in range(17, 21):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        for i in range(22, 26):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        for i in range(27, 30):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        for i in range(31, 35):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        for i in range(36, 41):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        cv2.line(frame, (shape.part(36).x, shape.part(36).y), (shape.part(41).x, shape.part(41).y), (0, 255, 0), 2)
        for i in range(42, 47):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        cv2.line(frame, (shape.part(42).x, shape.part(42).y), (shape.part(47).x, shape.part(47).y), (0, 255, 0), 2)
        for i in range(48, 59):
            cv2.line(frame, (shape.part(i).x, shape.part(i).y), (shape.part(i+1).x, shape.part(i+1).y), (0, 255, 0), 2)
        cv2.line(frame, (shape.part(48).x, shape.part(48).y), (shape.part(59)))

import cv2
import dlib

# Load the pre-trained facial landmark detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    # Loop through each detected face
    for face in faces:
        # Get the facial landmarks for the face
        landmarks = predictor(gray, face)

        # Draw the face outline
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

        # Loop through each facial landmark and draw its outline
        for i in range(68):
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()

import cv2
import dlib

# Load face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    # Iterate over detected faces
    for face in faces:
        # Get facial landmarks for the face
        landmarks = predictor(gray, face)

        # Draw facial landmarks on the frame
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Draw face outline
        shape = predictor(gray, face)
        for i in range(1, 17):
            x = shape.part(i).x
            y = shape.part(i).y
            x2 = shape.part(i-1).x
            y2 = shape.part(i-1).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 2)

        # Draw eyes, nose and mouth outlines
        for i in range(36, 42):
            x = shape.part(i).x
            y = shape.part(i).y
            x2 = shape.part(i+1).x
            y2 = shape.part(i+1).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 2)
        for i in range(42, 48):
            x = shape.part(i).x
            y = shape.part(i).y
            x2 = shape.part(i+1).x
            y2 = shape.part(i+1).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 2)
        for i in range(29, 36):
            x = shape.part(i).x
            y = shape.part(i).y
            x2 = shape.part(i+1).x
            y2 = shape.part(i+1).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 2)

    # Display frame in a window
    cv2.imshow('Video', frame)

    # Wait for user to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
