import numpy
import cv2

img = numpy.zeros((3, 3), dtype=numpy.uint8)

print(img)

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

print(img)

print(img.shape)
