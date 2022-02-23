import cv2 as cv


# img = cv.imread('r6.jpg')


# cv.imshow('r6',img)
#cv.waitKey(0)

capture = cv.VideoCapture('apex1.mp4')


while True:
	isTrue,frame = capture.read()

	cv.imshow('apex',frame)

	resize = cv.resize(frame,(frame.shape[1]//2,frame.shape[0]//2),interpolation = cv.INTER_CUBIC)
	cv.imshow('re',resize)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()

cv.destroyAllWindows()

