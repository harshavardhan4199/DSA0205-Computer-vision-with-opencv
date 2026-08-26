import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)
for i, (im, title) in enumerate(zip([binary, eroded], ['Binary', 'Eroded'])):
    plt.subplot(1, 2, i+1)
    plt.imshow(im, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
