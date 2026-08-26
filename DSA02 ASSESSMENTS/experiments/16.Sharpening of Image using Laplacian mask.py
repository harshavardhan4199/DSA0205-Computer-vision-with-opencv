import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)  
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
lap = cv2.filter2D(img, -1, kernel)
sharp = cv2.subtract(img, lap)

plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(sharp, cmap='gray'), plt.title("Sharpened"), plt.axis('off')
plt.show()
