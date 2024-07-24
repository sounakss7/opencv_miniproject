import cv2
img_color = cv2.imread("C:\\Users\\souna\\OneDrive\\Desktop\\IMAGES\\CR7.jpg")
cv2.imshow('Color Image', img_color)
cv2.waitKey(0)
cv2.imwrite("C:\\Users\\souna\\OneDrive\\Desktop\\IMAGES\\kaka.jpg", img_color)