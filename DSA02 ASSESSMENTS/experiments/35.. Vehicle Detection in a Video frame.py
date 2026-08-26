import cv2

# Load the classifier from the correct path
cascade_path = r"C:\Users\hv364\Downloads\traffic video.mp4"
vehicle_cascade = cv2.CascadeClassifier(cascade_path)

if vehicle_cascade.empty():
    print("Error: Could not load vehicle cascade XML file.")
else:
    cap = cv2.VideoCapture(r"C:\Users\hv364\Downloads\traffic.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
