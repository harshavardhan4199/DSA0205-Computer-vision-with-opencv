import cv2
import numpy as np
image = cv2.imread(r"C:\Users\hv364\Downloads\tiger image.jpeg")
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
canvas[100:100+image.shape[0], 100:100+image.shape[1]] = image
cv2.imshow('Moved Image', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
