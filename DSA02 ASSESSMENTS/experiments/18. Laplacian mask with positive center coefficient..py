import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
lap = cv2.filter2D(img, -1, np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))
sharp = cv2.filter2D(img, -1, np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))

for i, (im, title) in enumerate(zip([img, lap, sharp], ['Original', 'Laplacian', 'Sharpened'])):
    plt.subplot(1, 3, i+1), plt.imshow(im, cmap='gray'), plt.title(title), plt.axis('off')
plt.tight_layout(), plt.show()
