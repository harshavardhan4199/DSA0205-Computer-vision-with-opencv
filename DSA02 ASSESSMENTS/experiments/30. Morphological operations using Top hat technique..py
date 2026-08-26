import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)

kernel = np.ones((9, 9), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

for i, (im, title) in enumerate(zip([img, tophat], ['Original', 'Top Hat'])):
    plt.subplot(1, 2, i+1)
    plt.imshow(im, cmap='gray')
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()
