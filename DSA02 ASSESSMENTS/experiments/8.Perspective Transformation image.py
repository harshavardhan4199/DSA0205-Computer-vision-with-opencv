import cv2
import numpy as np
image = cv2.imread(r"C:\Users\hv364\Downloads\eye.jpeg")
pts1 = np.float32([[50, 50], [400, 50], [50, 300], [400, 300]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (300, 300))
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
