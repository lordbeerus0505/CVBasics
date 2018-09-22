"""
    Applications include extracting foreground from background

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('bentley.jpg',cv2.IMREAD_GRAYSCALE)
#use bentley, stark ,yellow as well
# cv2.imshow('image',img)
# fgbg = cv2.BackgroundSubtractor()
w,h=img.shape[:2]
print(w,h) #dimensions have been found


thresh=150
image=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)[1]
fig=plt.figure()
plt.imshow(image,cmap=plt.cm.gray)
plt.show()


# for i in range(300,450):
#     for j in range(350,380):
#         img[i,j]=img[200,650+j-380]
# for i in range(320,470):
#     for j in range(380,430):
#         img[i,j]=img[200,650+j-380]
# for i in range(330,450):
#     for j in range(430,450):
#         img[i,j]=img[200,700+j-440]
# for i in range(350,420):
#     for j in range(450,470):
#         img[i,j]=img[200,710]

#instead with a single condition
# for j in range(350,470):
#     if j>350 and j<=355:
#         for i in range(340,435):
#             img[i,j]=img[200,650]
#     elif j<360:
#         for i in range(340,445):
#             img[i,j]=img[200,655]
#     elif j<365:
#         for i in range(338,450):
#             img[i,j]=img[200,657]
#     elif j<370:
#         for i in range(338,452):
#             img[i,j]=img[200,657]
#     elif j<375:
#         for i in range(336,455):
#             img[i,j]=img[200,658]
#     elif j<380:
#         for i in range(336,455):
#             img[i,j]=img[200,658]
#     elif j<385:
#         for i in range(330,465):
#             img[i,j]=img[200,658]
#     elif j<390:
#         for i in range(329,467):
#             img[i,j]=img[200,659]
#     elif j<395:
#         for i in range(327,469):
#             img[i,j]=img[200,659]
#     elif j<400:
#         for i in range(325,473):
#             img[i,j]=img[200,658]
#     elif j<405:
#         for i in range(323,475):
#             img[i,j]=img[200,658]
#     elif j<410:
#         for i in range(322,476):
#             img[i,j]=img[200,658]
#     elif j<415:
#         for i in range(320,478):
#             img[i,j]=img[200,658]
#     elif j<420:
#         for i in range(322,476):
#             img[i,j]=img[200,658]
    
        


        

cv2.imshow('image',img)
# plt.imshow(img)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
