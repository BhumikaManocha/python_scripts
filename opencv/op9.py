# -*- coding: utf-8 -*-
"""
   detects only blue colour

@author: vansh
"""

import cv2
import numpy as np

def main():
    windowName = 'video capture'
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)   
    if cap.isOpened():
        ret, img = cap.read()
    else:
        ret=False
        
    while ret:
        
        ret, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #blue color
        low = np.array([100, 50, 50])        
        high=np.array([140, 255, 255])
        mask = cv2.inRange(hsv, low, high)
        res = cv2.bitwise_and(img,img,mask=mask)
        
        cv2.imshow(windowName, img)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.DestroyAllWindows()
    
if __name__ == "__main__":
    main()
