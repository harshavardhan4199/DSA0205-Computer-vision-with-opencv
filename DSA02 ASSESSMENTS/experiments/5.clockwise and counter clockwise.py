import cv2
path = r"C:\Users\hv364\Downloads\dolphin.jpeg"
image = cv2.imread(path)

if image is None:
    print("Error: Could not load image.")
    exit()
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original", image)
cv2.imshow("Rotated 90° Clockwise", clockwise)
cv2.imshow("Rotated 90° Counter-Clockwise", counter_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
