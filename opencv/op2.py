# -*- coding: utf-8 -*-
"""
   understanding the color concepts
@author: vansh
"""

import cv2
import numpy as np

def main():
    img1=np.zeros((512, 512, 3), np.uint8)
    cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
    cv2.rectangle(img1, (100, 99), (200, 200), (255, 255, 0), 2)
    cv2.imshow('pic',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()