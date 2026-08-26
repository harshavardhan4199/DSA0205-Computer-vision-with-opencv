import cv2
import numpy as np
cap = cv2.VideoCapture(r"C:\Users\hv364\Downloads\diving in sea.mp4")  
src_pts = np.float32([[50, 50], [400, 50], [50, 300], [400, 300]])
dst_pts = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(src_pts, dst_pts)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    warped_frame = cv2.warpPerspective(frame, M, (300, 300))
    cv2.imshow('Original', frame)
    cv2.imshow('Perspective Transformed', warped_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
