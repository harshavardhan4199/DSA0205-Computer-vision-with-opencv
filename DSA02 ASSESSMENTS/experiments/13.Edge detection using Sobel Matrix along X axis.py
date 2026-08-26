import cv2
import numpy as np
img = cv2.imread(r"C:\Users\hv364\Downloads\bird image.jpeg", cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
cv2.imshow('Original Image', img)
cv2.imshow('Sobel X Edge Detection', abs_sobel_x)
cv2.imwrite('sobel_x_edges.jpg', abs_sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
