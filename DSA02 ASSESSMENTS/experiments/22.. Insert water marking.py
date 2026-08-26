import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg")
watermarked = img.copy()
cv2.putText(watermarked, 'Watermark', (50, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
for i, (im, title) in enumerate(zip([img, watermarked], ['Original', 'Watermarked'])):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
