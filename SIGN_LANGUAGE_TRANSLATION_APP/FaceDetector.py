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