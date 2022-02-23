import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('dogs.jpg')
cv.imshow('dog',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
mask  = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)


masked = cv.bitwise_and(gray,gray,mask= mask)
cv.imshow('mask',masked)

gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('gray hist')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

### for colored img
# plt.figure()
# plt.title('color hist')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')

# colors = ('b','g','r')

# for i, col in enumerate(colors):
# 	hist = cv.calcHist([img],[i],None,[256],[0,256])
# 	plt.plot(hist,color = col)
# 	plt.xlim([0,256])


# plt.show()


cv.waitKey(0)