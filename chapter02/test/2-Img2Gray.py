import cv2



grayImage = cv2.imread('../MyPic.jpg', cv2.IMREAD_GRAYSCALE)

print(grayImage.shape) #(290, 290)
print(cv2.imread('../MyPic.jpg').shape) #(290, 290, 3)

cv2.imwrite('MyPicGray.png', grayImage)


