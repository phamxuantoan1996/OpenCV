'''
1) Changing Colorspace
- Learn to change images between different color spaces. Plus learn to track a 
colored object in a video.

- Goal:
+ In this tutorial, you will learn how to convert images from one color-space to
another, like BRG <-> Gray, BGR <-> HSV.
+ In addition to that, we will create an application which extracts a colored object 
in a video
+ You will learn following functions : cv2.cvtColor(), cv2.inRange() etc.

- For color conversion, we use the function cv2.cvtColor(input_image,flag) where flag
determines the type of conversion.

- For BGR -> Gray conversion we use the flags cv2.COLOR_BGR2GRAY
- For BGR -> HSV conversion we use the flag cv2.COLOR_BGR2HSV
- Note : For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range
is [0,255]. 

* Object tracking
Now we know how to convert BGR image to HSV, we can use this to extract a colored 
object. In HSV, it is more easier to represent a color than RGB color-space. In our
application, we will try extract a blue colored object. So here is method:
+ Take frame of video
'''
# change color space
# import cv2
# import numpy as np
# capture = cv2.VideoCapture(0)
# while True:
#     _,frame = capture.read()
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     # define range of blue color in HSV
#     lower = np.array([105, 130, 30])
#     upper = np.array([126, 255, 255])
#     mask = cv2.inRange(hsv,lower,upper)
#     result = cv2.bitwise_and(frame,frame,mask=mask)
#     cv2.imshow("frame",frame)
#     cv2.imshow("mask",mask)
#     cv2.imshow("result",result)
#     if cv2.waitKey(1) == ord(' '):
#         break
# capture.release()
# cv2.destroyAllWindows()

# thresholding
import cv2
import numpy as np

img = cv2.imread("image/nap-chai.jpg",cv2.IMREAD_GRAYSCALE)

thres1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,12)
# thres2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,12)


cv2.imshow("image1",thres1)
# cv2.imshow("image2",thres2)

cv2.waitKey(0)

cv2.destroyAllWindows()