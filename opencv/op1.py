# -*- coding: utf-8 -*-
"""
   simple code (will be edited in furure)
@author: vansh
"""

import cv2

def main():
    #print(cv2.__version__)
    img_path="E:\\vansh\\work\\opencv\\standard_test_images\\4.1.04.tiff"
    path="E:\\vansh\\work\\opencv\\lena.jpg"
    img=cv2.imread(img_path)
    #cv2.namedWindow('pic',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('pic',img)
    cv2.imwrite(path,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.destroyWindow('pic')
    
if __name__=="__main__":
    main()
