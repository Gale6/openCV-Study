import cv2 as cv
import numpy as np

img = cv.imread('r6.jpg')
cv.imshow('r6',img)


def translate(img,x,y):
	transMat = np.float32([[1,0,x],[0,1,y]])
	dimensions = (img.shape[1],img.shape[0])
	return cv.warpAffine(img,transMat,dimensions)
def rotate(img,angle,rotPoint= None):
	(height,width) = img.shape[:2]
	if rotPoint == None:
		rotPoint = (width//2,height//2)
	rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
	dimensions = (width,height)

	return cv.warpAffine(img,rotMat,dimensions)

translated = translate(img,100,100)
cv.imshow('translated',translated)

rotated = rotate(img,45)
cv.imshow('rotated',rotated)


resized = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),interpolation = cv.INTER_CUBIC)
cv.imshow('resized',resized)

fliped = cv.flip(img,-1)
cv.imshow('fliped',fliped)

cv.waitKey(0)
