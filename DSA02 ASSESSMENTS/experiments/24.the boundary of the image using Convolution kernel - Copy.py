import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])
boundary = cv2.filter2D(img, -1, kernel)
for i, (im, title) in enumerate(zip([img, boundary], ['Original', 'Boundary'])):
    plt.subplot(1, 2, i+1)
    plt.imshow(im, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
