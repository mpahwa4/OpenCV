import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# channels = blue, green, red

b,g,r = cv.split(img)

cv.imshow('Blue', b) # shows gray scale img, lighter pixels = higher concentration of color
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape) # 3rd element = number of channels (b,g,r)
print(b.shape) # no 3rd element, as there is only 1 channel
print(g.shape)
print(r.shape)

# merging channels

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# isolating each channel

blue = cv.merge([b, blank, blank]) # setting other channels to blank
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)