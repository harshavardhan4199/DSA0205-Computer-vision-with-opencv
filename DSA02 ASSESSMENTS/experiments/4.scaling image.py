import cv2
img = cv2.imread(r"C:\Users\hv364\Downloads\hanuman walpaper.webp")
if img is None:
    print("Error: Image not loaded. Please check the file path.")
else:
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    bigger = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Original", img)
    cv2.imshow("Smaller", smaller)
    cv2.imshow("Bigger", bigger)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

