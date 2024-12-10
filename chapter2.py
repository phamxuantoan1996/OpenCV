'''
Chapter 2: Handling File, Cameras and GUIs
* Introduces OpenCV's I/O functionality.
* Discuss a project concept and the beginnings of an object-oriented design for 
this project.

2.1) Basic I/O Script
- All CV applications need to get images as input. Most also need to produce images
as output. 
- An interactive CV application might require a camera as an input source and a
window as a output destination.

2.2) Reading/Writing an image file
- OpenCV provides the imread() and imwrite() functions that support various file 
formats for still images. 

- Images can be loaded from one file format and saved to another by using imread()
and imwrite().

- imread() returns and image in BGR color format.

- we may specify the mode of imread() to be CV_LOAD_IMAGE_COLOR, 
CV_LOAD_IMAGE_GRAYSCALE, or CV_LOAD_IMAGE_UNCHANGE.

2.3) Converting between an image and raw bytes.
- An OpenCV image is a 2D or 3D array of type numpy.array. Example, an 8bit grayscale
image is a 2D array containing byte values. A 24bit BGR image is a 3D array, also
containing byte values. 

- We may access these values by using expression like image[0,0] or image[0,0,0].
The first index is the pixel's y coordinate (row). The second index is the 
pixel's x coordinate (colunm). The third index represent a color channel.

- For example, in an 8bit gray-scale image with a white pixel in the upper-left 
conner, image [0,0] is 255. For a 24bit BGR image with a blue pixel in the 
upper-left conner, image [0,0] is [255,0,0].

- Provided that an image has 8 bits per channel, we can case it to a standard Python
bytearray, which is one-dimensional:

-> byteArray = bytearray(image)

2.4 Reading/Writing a video file.
- OpenCV provides the VideoCapture and VideoWriter classes that support various
video file formats. The supported formats vary by system but should always include
AVI. Via its read() method, a VideoCapture class may be polled for new frames until
reaching the end of it video. 

- Each frame is an image in BGR format. An image may be passed to the write()
method of the VideoWriter class, which appends the the image to the file in 
VideoWriter. 

2.5 Capturing camera frames
- A stream of camera frames is represented by VideoCapture class.

2.6. Displaying camera frame in a window
- OpenCV allows named windows to be created, redrawn, and destroyed using the
namedWindow() , imshow() , and destroyWindow() functions.

-any window may capture keyboard input via the waitKey() function and mouse input 
via the setMouseCallback() function.

- The argument to waitKey() is a number of ms to wait for keyboard in put. The 
return value is either -1 or an ASCII keys.
- Function ord() can convert a character to its ASCII keycode.

- The callback's event argument is one of the following:
+ cv2.cv.CV_EVENT_MOUSEMOVE : Mouse movement
+ cv2.cv.CV_EVENT_LBUTTONDOWN : Left button down
+ cv2.cv.CV_EVENT_RBUTTONDOWN : Right button down
+ .......................



'''
# import cv2
# img = cv2.imread('image/tomato.jpg',cv2.IMREAD_COLOR)
# img = cv2.imread('image/tomato.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('image/tomato.jpg',cv2.IMREAD_UNCHANGED)
# for i in range(0,612):
#     img[306,i] = [0,0,0]
# for i in range(0,612):
#     img[i,306] = [0,0,0]
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy
# import cv2
# import os
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = numpy.array(randomByteArray)
# grayImage = flatNumpyArray.reshape(300,400)
# brgImage = flatNumpyArray.reshape(100,400,3)
# cv2.imshow('image',brgImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy
# import cv2
# import os
# randomArray = bytearray(os.urandom(27))
# flatNumpyArray = numpy.array(randomArray)
# rgbImage = flatNumpyArray.reshape(3,3,3)
# rgbImage[2,1] = [0,0,0]
# arr = bytearray(rgbImage)
# for i in range(0,3):
#     print('index ',i,':',arr[(2*3+1)*3 + i])
# cv2.imshow('img',rgbImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# img = cv2.imread('image/tomato.jpg',cv2.IMREAD_COLOR)
# print(img[306,306])
# arr = bytearray(img)
# index = (306*612+306)*3
# print(arr[index])
# print(arr[index + 1])
# print(arr[index + 2])


#capture frame from camera and save.
import cv2
#open the default camera
cam = cv2.VideoCapture(0)
#Get the default frame width and height
frameWidth = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeigh = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
#define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('ouput.mp4',fourcc,20,(frameWidth,frameHeigh))
while True:
    ret,frame = cam.read()
    #write the frame to the output file
    out.write(frame)
    #display the capture frame
    cv2.imshow("camera",frame)
    #press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()


#read frame from a video file
# import cv2
# videoCapture = cv2.VideoCapture('output.mp4')
# if videoCapture.isOpened():
#     print("video is opened")
# fps = videoCapture.get(cv2.CAP_PROP_FPS)
# frameWidth = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
# frameHeigh = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# while videoCapture.isOpened():
#     ret,frame = videoCapture.read()
#     if ret == True:
#         cv2.imshow('video',frame)
#         if cv2.waitKey(50) == ord('q'):
#             break
#     else:
#         break
# videoCapture.release()
# cv2.destroyAllWindows()


#Displaying camera frames in a window
# import cv2
# click = False
# def onMouse(event,x,y,flags,param):
#     global click
#     if event == cv2.EVENT_LBUTTONUP:
#         click = not click
# if __name__ == '__main__':
#     videoCapture = cv2.VideoCapture(0)
#     cv2.namedWindow('window1')
#     cv2.setMouseCallback('window1',onMouse)
#     while True:
#         ret,frame = videoCapture.read()
#         if ret:
#             cv2.imshow("window1",frame)
#         if cv2.waitKey(1) == ord('q') or click:
#             break
#     videoCapture.release()
#     cv2.destroyAllWindows()


