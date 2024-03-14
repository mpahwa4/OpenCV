import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)

# masking allows us to focus on certain parts of images (eg. focusing on faces)

blank = np.zeros(img.shape[:2], dtype='uint8') # dimensions of mask must be of same size of image

mask_circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask_circle)

mask_rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(mask_circle, mask_rectangle)
cv.imshow('Weird Shape', weird_shape)

masked_img = cv.bitwise_and(img, img, mask=mask_circle)
cv.imshow('Masked Image', masked_img)

masked_img2 = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked Image 2', masked_img2)

cv.waitKey(0)