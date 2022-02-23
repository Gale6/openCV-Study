import cv2 as cv


def rersaleFrame(frame,scale=.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width,height)

	return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)



img = cv.imread('r6.jpg')
resizeImg = rersaleFrame(img,.25)

cv.imshow('r6',img)
cv.imshow('r5',resizeImg)

cv.waitKey(0)

capture = cv.VideoCapture('apex1.mp4')
while True:

	isTrue,frame = capture.read()

	frame_resized = rersaleFrame(frame,.25)

	cv.imshow('apex',frame)
	cv.imshow('apex2',frame_resized)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()

cv.destroyAllWindows()

