import cv2

cascPath = 'data.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(48, 48),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # Press 'q' to exit infinite image processing loop
        break


capture.release()
cv2.destroyAllWindows()
