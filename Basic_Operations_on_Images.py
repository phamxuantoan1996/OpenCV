'''
Goal:
+ Access pixel values and modify them
+ Acess image properties
+ Setting Region of Image (ROI)
+ Spliting and Merging images.

1.Accessing and Modifying pixel values
Example:
print(img[100,100]) -> [255,255,255]
print(img[100,100,0]) -> B = 255

array.item(100,100,2) -> accessing red value
array.item((100,100,2),100) -> modifying red value.

2. Acessing Image Property
+ img.shape : row,column,channel
+ img.size : total number of pixels
+ img.dtype : image datatype

3. Image ROI.

4. Spliting and Merging Image Channels.
The B,G,R channels of an image can be split into their individual planes when
needed.
Then, the individual channels can be merged back together to form a BGR image 
again.


'''

#image roi
# import cv2
# import numpy as np
# img = cv2.imread('image/tomato.jpg')
# roi = img[40:575,55:565]
# cv2.imshow('window1',roi)
# cv2.waitKey()
# cv2.destroyAllWindows()

#spliting and merging
# import cv2
# import numpy as np
# img = cv2.imread('image/tomato.jpg')

# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))
# or
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]

#make all the blue pixel to zero
# img[:,:,0] = 0
#make all the green pixel to zero
# img[:,:,1] = 0
#make all the red pixel to zero
# img[:,:,2] = 0

# cv2.imshow('window1',img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#making borders for image
import cv2
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv2.imread('image/tomato.jpg')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()