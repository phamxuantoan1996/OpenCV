
import cv2
import numpy as np
x0 = -1
y0 = -1
def onMouse(event,x,y,flag,argument):
    global x0
    global y0
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img,center=(x,y),radius=2,color=(255,255,255),thickness=1)
        if x0 >= 0 and y0 >= 0:
            cv2.line(img=img,pt1=(x0,y0),pt2=(x,y),color=(255,0,0))
        x0 = x
        y0 = y

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("window1")

cv2.setMouseCallback("window1",onMouse)

while True:
    cv2.imshow('window1',img)
    key = cv2.waitKey(10)
    if key == ord(' '):
        break
    if key == ord('c'):
        x0 = -1
        y0 = -1
        img = np.zeros((512,512,3),np.uint8)
cv2.destroyAllWindows()
