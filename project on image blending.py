# import cv2
# import numpy as np
#
# def nothing(x):
#     pass
#
# # Create a named window
# cv2.namedWindow('Blended Image')
#
# # Load two images
# img1 = cv2.imread('hadi.jpeg')
# img1=cv2.resize(img1,(500,500))
# img2 = cv2.imread('haider.jpg')
# img2=cv2.resize(img2,(500,500))
#
# # Create a trackbar for blending ratio
# cv2.createTrackbar('Blend', 'Blended Image', 0, 100, nothing)
#
# while True:
#     # Get trackbar position
#     blend_ratio = cv2.getTrackbarPos('Blend', 'Blended Image')
#     n=blend_ratio/100
#
#     # Blend images
#     blended_img = cv2.addWeighted(img1, n, img2, 1 - n, 0)
#
#     # Show blended image
#     cv2.imshow('Blended Image', blended_img)
#
#     # Break the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release resources
# cv2.destroyAllWindows()





# for practice purpose
# import cv2
# import numpy as np
# def cross(x):
#     pass
#
# # step#1 load and resize images
# img1=cv2.imread("hadi.jpeg")
# img1=cv2.resize(img1,(1000,1000))
# img2=cv2.imread("haider.jpg")
# img2=cv2.resize(img2,(1000,1000))
#
# # step#2 create trackbar radio
# cv2.namedWindow("blanding")
# cv2.createTrackbar("alpha","blanding",0,100,cross)
# while True:
#     tr=cv2.getTrackbarPos("alpha","blanding")/100
#     # bimg=cv2.addWeighted(img1,tr,img2,1-tr,0)
#     bimg=cv2.addWeighted(img1,1-tr,img2,tr,0)
#
#     cv2.imshow("blanding",bimg)
#     if cv2.waitKey(1) & 0xff==27:
#        break
#
# cv2.destroyAllWindows()

import cv2
import numpy as np
img1=cv2.imread("haider.jpg")
img1=cv2.resize(img1,(500,500))
img2=cv2.imread("hadi.jpeg")
img2=cv2.resize(img2,(500,500))

# now creating trackbar
cv2.namedWindow("wn")
def cross(x):
    pass
cv2.createTrackbar("alpha","wn",0,100,cross)

while True:
    br=cv2.getTrackbarPos("alpha","wn")/100
    bimg=cv2.addWeighted(img1,br,img2,1-br,0)
    cv2.imshow("wn",bimg)
    if cv2.waitKey(1)& 0xff==27:
        break
cv2.destroyAllWindows()
