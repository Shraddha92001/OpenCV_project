import cv2 as cv

img = cv.imread('image/aero1.jpg')

cv.imshow('AREA', img)
cv.waitKey(0)