import cv2
img = cv2.imread(r"C:\Users\hv364\Downloads\dolphin.jpeg")
x, y, w, h = 100, 100, 200, 150  
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
extracted = img[y:y+h, x:x+w]
cv2.imshow("Rectangle", img)
cv2.imshow("Extracted Object", extracted)
cv2.waitKey(0)
cv2.destroyAllWindows()
