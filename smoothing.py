import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# use smoothing to reduce noise

# averaging - makes the middle pixel intensity the average of the outer pixels' intensities
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# gaussian blur - does the same thing as averaging, but there is a weight tied to each pixel
# usually more natural than averaging
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# median blur - makes the middle pixel the median of the surrounding pixels
# usually more effective at removing noise and usually prefers lower kernel sizes (eg. 3)
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# bilateral blur - applies blurring but retains the edges in the image
# most effective way of blurring
bilateral = cv.bilateralFilter(img, 10, 35, 25) # larger value of sigma space means pixels further away impact the pixel in question
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)