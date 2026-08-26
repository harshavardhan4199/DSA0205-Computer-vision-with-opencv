import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
laplacian = cv2.filter2D(img, -1, kernel)
sharpened = cv2.subtract(img, laplacian)

plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(133), plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.tight_layout(), plt.show()
