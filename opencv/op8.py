# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:09:31 2018

@author: vansh
"""

import cv2
cap=cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    #print(ret)
    #print(img)
    
    cv2.imshow('img',img)
    cv2.waitKey(10)
    
cap.release()
cv2.destroyAllWindows()

                     
                     