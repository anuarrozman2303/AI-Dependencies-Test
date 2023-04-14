import cv2 

img  = cv2.imread("image_1.jpg")

resize_img = cv2.resize(img, (640,480))

cv2.imwrite("Resize_Image.jpg", resize_img)