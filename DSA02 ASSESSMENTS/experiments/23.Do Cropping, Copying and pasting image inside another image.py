import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg")
crop_top, crop_bottom = 50, 150
crop_left, crop_right = 100, 200
cropped = img[crop_top:crop_bottom, crop_left:crop_right]
h, w = cropped.shape[:2]
paste_top, paste_left = 10, 10 
paste_bottom = paste_top + h
paste_right = paste_left + w
pasted = img.copy()
pasted[paste_top:paste_bottom, paste_left:paste_right] = cropped
for i, (im, title) in enumerate(zip([img, pasted], ['Original', 'Crop & Pasted'])):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
