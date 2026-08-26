import cv2
img = cv2.imread(r"C:\Users\hv364\Downloads\bird image.jpeg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (5, 5), 1.4)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite('canny_edges.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
