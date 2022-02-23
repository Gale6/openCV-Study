import cv2 as cv
import numpy as np


img = cv.imread('r6.jpg')


blank = np.zeros((500,500),dtype='uint8')

# img[:] = 0,0,255


cv.rectangle(img,(img.shape[1],img.shape[0]),(img.shape[1]//2,img.shape[0]//2),(0,255,0),thickness = -1)

print(img)
cv.imshow('r6',img)

cv.waitKey(0)