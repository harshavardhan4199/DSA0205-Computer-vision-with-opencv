import cv2
import numpy as np
image = cv2.imread(r"C:\Users\hv364\Downloads\fruit.jpeg")  
if image is None:
    print("Error: Could not load image.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)
    cv2.imshow('Original', image)
    cv2.imshow('Dilated Image', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
