import numpy as np

import cv2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)


face_cascade = cv2.CascadeClassifier('/home/pi/opencv-2.4.11/data/haarcascades/haarcascade_frontalface_alt.xml')

cap=cv2.VideoCapture(0)

while(1):

    ret, img = cap.read()
    GPIO.output(18,GPIO.HIGH)

    if ret:

        height, width, channels = img.shape

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        res = cv2.resize(gray,(width/4, height/4), interpolation = cv2.INTER_LINEAR)

        gray2 = cv2.equalizeHist(res)

        face = face_cascade.detectMultiScale(gray2, scaleFactor=1.1,

        minNeighbors=5,

        minSize=(30, 30),

        flags = cv2.cv.CV_HAAR_SCALE_IMAGE

        )

        for (x,y,w,h) in face:

            #cv2.rectangle(img,(x*4,y*4),((x+w)*4,(y+h)*4),(255,0,0),0)

            print 1
            #GPIO.output(18,GPIO.HIGH)
        #cv2.imshow('img',img)

        
	#GPIO.output(18,GPIO.LOW)
        if(cv2.waitKey(1)=='q'):

            cap.release()

            cv2.destroyAllWindows()

            break
