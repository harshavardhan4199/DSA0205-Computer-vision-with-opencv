import cv2
image = cv2.imread(r"C:\Users\hv364\Downloads\lion.jpg")  
if image is None:
    print("Error: Image not found.")
else:
    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blurred Image', blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
