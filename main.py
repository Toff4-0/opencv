#!~/testcam/bin/python3
# -*- coding: utf-8 -*- 
import sys
import cv2
import numpy as np



Cap = cv2.VideoCapture(0)

Cap.set(39, 0) # desactive l'autofocus (1 pour activer)
Cap.set(28, 0) # valeur de focus est le param n°28
Cap.set(5,30) # valeur de fps param n° 5

# Check if camera opened successfully
if (Cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(Cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = Cap.read()
  if ret == True:
    blurred = cv2.GaussianBlur(frame, (13, 13), 0)
    cimg = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)  
    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, cimg.shape[0]/64, param1=50, param2=40, minRadius=20, maxRadius=30)
    
    if circles is not None:
        cir_len = circles.shape[1] # store length of circles found
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            # print du raduis 
            #print('radius= ',i[2])
    else:
        cir_len = 0 # no circles detected
          


    # Display the resulting frame
    cv2.imshow('Frame',frame)
    #cv2.imshow('img',cimg)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()