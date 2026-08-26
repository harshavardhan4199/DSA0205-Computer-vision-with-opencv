import cv2
import numpy as np
img = cv2.imread(r"C:\Users\hv364\Downloads\bird image.jpeg", cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)
cv2.imshow('Original Image', img)
cv2.imshow('Sobel XY Edge Detection', gradient_magnitude)
cv2.imwrite('sobel_xy_edges.jpg', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
