import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg", 0)
kernel_x = np.array([[-1, -2, -1],
                     [ 0,  0,  0],
                     [ 1,  2,  1]])
kernel_y = np.array([[-1,  0,  1],
                     [-2,  0,  2],
                     [-1,  0,  1]])
grad_x = cv2.filter2D(img, -1, kernel_x)
grad_y = cv2.filter2D(img, -1, kernel_y)
sharpened = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
for i, (im, title) in enumerate(zip([img, sharpened], ['Original', 'Gradient Sharpened'])):
    plt.subplot(1, 2, i+1), plt.imshow(im, cmap='gray'), plt.title(title), plt.axis('off')
plt.tight_layout(), plt.show()
