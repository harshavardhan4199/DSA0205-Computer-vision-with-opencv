import cv2
import numpy as np
image = cv2.imread(r"C:\Users\hv364\Downloads\tree image.jpeg")
src_pts = np.float32([[100, 100], [400, 100], [100, 300], [400, 300]])
dst_pts = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
H, status = cv2.findHomography(src_pts, dst_pts)
transformed_image = cv2.warpPerspective(image, H, (300, 300))
cv2.imshow('Original', image)
cv2.imshow('Homography Transformed', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
