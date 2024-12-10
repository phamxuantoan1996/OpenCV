'''
Goal:
- Learn several arithmetic operations on images like addition, subtraction, bitwise 
operations etc.
- You will learn these functions: cv2.add(), cv2.addWeighted() etc.

1) Image Addition
You can add two images by OpenCV function, cv2.add() or simply by numpy operation,
res = img1 + img2. Both images should be of same depth and type, or second image 
can just be a scalar value.

Example:
x = np.uint8([250])
x = np.uint8([10])
cv2.add(x,y)

2) Image Blending
This is also image addition, but different weights are given to images so that it
gives a feeling of blending or transparency. Images are add as per the equation
below:
    g(x) = (1-a).f0(x) + a.f1(x)

3) Bitwise Operation
This include bitwise AND, OR, NOT and XOR operations.



'''
#adding and blending
# import cv2
# import numpy as np
# import time
# img1 = cv2.imread("image/tomato.jpg")
# arr = bytearray([0]*img1.shape[0]*img1.shape[1]*img1.shape[2])
# img2 = np.array(arr)
# img2 = img2.reshape(img1.shape[0],img1.shape[1],img1.shape[2])
# img3 = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.2,gamma=0)
# cv2.imshow("image",img3)
# cv2.waitKey()
# cv2.destroyAllWindows()


import cv2
import numpy as np

img1 = cv2.imread("image/tomato.jpg")

arr = bytearray([0]*img1.shape[0]*img1.shape[1]*img1.shape[2])
img2 = np.array(arr)
img2 = img2.reshape(img1.shape[0],img1.shape[1],img1.shape[2])


delta = 0.0
while True:
    
    
    cv2.waitKey(1)
    delta = delta + 0.0005
    print(delta)
    if delta >= 1:
        break
    img3 = cv2.addWeighted(src1=img1,alpha=delta,src2=img2,beta=1-delta,gamma=0)
    cv2.imshow("image",img3)

cv2.waitKey()
cv2.destroyAllWindows()




