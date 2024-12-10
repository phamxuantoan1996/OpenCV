import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('color')
cv2.createTrackbar('R','color',0,255,nothing)
cv2.createTrackbar('G','color',0,255,nothing)
cv2.createTrackbar('B','color',0,255,nothing)

while True:
    cv2.imshow('color',img)
    r = cv2.getTrackbarPos('R','color')
    g = cv2.getTrackbarPos('G','color')
    b = cv2.getTrackbarPos('B','color')
    img[:] = [b,g,r]
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()