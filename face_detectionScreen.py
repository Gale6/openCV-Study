from PIL import ImageGrab
import cv2
import numpy as np
from numba import jit

face_cascade = cv2.CascadeClassifier('haar_face.xml')


def main():

    while True:
        screen = np.array(ImageGrab.grab(bbox=(0,0,2560,1440)))
        resized = cv2.resize(screen,(screen.shape[1]//3,screen.shape[0]//3),interpolation = cv2.INTER_CUBIC)
        gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        
        cor = cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
        for (x,y,w,h) in faces:
            
            cv2.rectangle(cor,(x,y),(x+w,y+h),(0,255,0),2)



        cv2.imshow('img',cor)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()