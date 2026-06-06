import cv2
image = cv2.imread("imageResizer\luffy.jpg")
#print(image.shape)
#cv2.imshow("luffy", image)
scale_percent = 50

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (width, height))
cv2.imwrite("imageResizer\\newimg.jpg", output)

cv2.waitKey(0)