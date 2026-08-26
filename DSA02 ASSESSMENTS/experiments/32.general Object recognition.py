import cv2

img_path = r"C:\Users\hv364\Downloads\watch.jpeg"
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to load image at {img_path}")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    objects = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Object Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
