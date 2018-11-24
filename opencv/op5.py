# -*- coding: utf-8 -*-
"""
        classifiers
        
@author: vansh
"""

#import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('4.1.03.tiff')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray, 1.3, 5)
                                
for (x,y,h,w) in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

print(faces)
print(type(faces))

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
                                    



