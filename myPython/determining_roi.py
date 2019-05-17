import cv2
import numpy as numpy

class determining_roi:

    #This method will return region of interest
    def getRoi(x,y,width,height):
        #Video Source File
        video = cv2.VideoCapture("mouthwash.avi")

        #Extracting first fram from video
        first_frame=video.read()
        
        roi=first_frame[y:y+height, x:x+width]

        #Printing First Frame from the video
        cv2.imshow("First Frame",first_frame)

        #Printing roi
        cv2.imshow("Region of Intereset",roi)

        return roi
