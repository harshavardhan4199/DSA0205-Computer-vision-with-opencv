import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
unsharp_mask = cv2.subtract(img, blur)
sharpened = cv2.add(img, unsharp_mask)
titles = ['Original', 'Blurred', 'Unsharp Mask', 'Sharpened']
images = [img, blur, unsharp_mask, sharpened]
for i in range(4):
    plt.subplot(1, 4, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.axis('off')
plt.tight_layout(), plt.show()
