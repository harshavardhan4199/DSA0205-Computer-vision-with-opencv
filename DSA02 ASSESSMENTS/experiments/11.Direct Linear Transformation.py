import numpy as np
import cv2
def compute_homography(src_pts, dst_pts):
    A = []
    for i in range(len(src_pts)):
        x, y = src_pts[i][0], src_pts[i][1]
        u, v = dst_pts[i][0], dst_pts[i][1]
        A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
        A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])
    A = np.array(A)
    U, S, Vt = np.linalg.svd(A)
    h = Vt[-1] / Vt[-1][-1]  
    H = h.reshape((3, 3))
    return H
src_pts = np.float32([[100, 100], [400, 100], [100, 300], [400, 300]])
dst_pts = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
H = compute_homography(src_pts, dst_pts)
image = cv2.imread(r"C:\Users\hv364\Downloads\elephant image.jpeg")
transformed = cv2.warpPerspective(image, H, (300, 300))
cv2.imshow('Original', image)
cv2.imshow('DLT Transformed', transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
