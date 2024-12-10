'''
1.Drawing Line
To draw a line, you need to pass starting and ending coordinates of line.
2.Drawing Rectangle
To draw a rectangle, you need to pass top-left corner and bot-right corner.
3.Draw Circle
To draw a circle, you need pass its center coordinates and radius.
4. Draw polyline

*****************************************************
Note: NumPy Array Reshaping
- Reshaping means changing the shape of an array.
- The shape of an array is the number of elements in each dimension.
- By reshaping we can add or remove dimensions or change number of elements in each
dimension.

Example : Convert the following 1-D array with 12 elements into a 2-D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)

Example : Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)

- Unknown Dimension
You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the dimensions 
in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.

Example:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)

- converting a multidimensional array into a 1D array.
Example:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
*****************************************************
5. Adding Text to Image
To put texts in images, you need specify following things:
• Text data that you want to write
• Position coordinates of where you want put it (i.e. bottom-left corner where 
data starts).
• Font type (Check cv2.putText() docs for supported fonts)
• Font Scale (specifies the size of font)
• regular things like color, thickness, lineType etc. For better look, 
lineType = cv2.LINE_AA is recommended.
'''

import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
# cv2.line(img=img,pt1=(0,0),pt2=(511,511),color=(255,0,0))
# cv2.line(img=img,pt1=(511,0),pt2=(0,511),color=(255,0,0))
# cv2.rectangle(img=img,pt1=(156,156),pt2=(356,356),color=(255,0,0))
# cv2.circle(img=img,center=(256,256),radius=100,color=(255,0,0))
# cv2.ellipse(img=img,center=(256,256),axes=(100,25),angle=45,startAngle=0,endAngle=360,color=(255,0,0))
#polyline
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img=img,pts=[pts],isClosed=True,color=(0,255,255))
#text
font = cv2.FONT_ITALIC
cv2.putText(img=img,text='OpenCV',org=(256,256),fontFace=font,fontScale=2,color=(255,0,0),thickness=1,lineType=cv2.LINE_AA)


cv2.imshow('window',img)
cv2.waitKey()
cv2.destroyAllWindows()