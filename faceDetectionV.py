import cv2 as cv

# img = cv.imread('r6.jpg')


# cv.imshow('r6',img)
#cv.waitKey(0)


def main():
	capture = cv.VideoCapture(0)


	while True:
		isTrue,frame = capture.read()
		resize = cv.resize(frame,(frame.shape[1]//2,frame.shape[0]//2),interpolation = cv.INTER_CUBIC)
		#cv.imshow('re',resize)

		gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
		haar_cascade = cv.CascadeClassifier('haar_face.xml')
		faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)
		for (x,y,w,h) in faces_rect:
			cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
		cv.imshow('detectedFaces',frame)



		if cv.waitKey(20) & 0xFF==ord('d'):
			break

	capture.release()

	cv.destroyAllWindows()
main()