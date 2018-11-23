"""
                A color trackbar

@author: vansh
"""

import cv2
import numpy as np

def cbfunc():
    pass

def main():
    windowName='opencv BGR Color tracker'
    img1=np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow(windowName)
    cv2.createTrackbar('Blue', windowName, 0, 255, cbfunc)
    cv2.createTrackbar('Green', windowName, 0, 255, cbfunc)
    cv2.createTrackbar('Red', windowName, 0, 255, cbfunc)
    
    
    while(True):
        cv2.imshow(windowName, img1)
        
        if cv2.waitKey(1) == 27:    #27 is character for escape button
            break
        blue = cv2.getTrackbarPos('Blue', windowName)
        green = cv2.getTrackbarPos('Green', windowName)
        red = cv2.getTrackbarPos('Red', windowName)
        img1[:] = [blue, green, red]
    
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()