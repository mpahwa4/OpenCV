import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Painting the image a certain colour
blank[:] = 0,0,255 # red
cv.imshow('Red', blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow('Mix', blank)

# Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (255,0,0), thickness=3)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (100,250), (300, 400), (0,0,0), thickness=3)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hello!', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)