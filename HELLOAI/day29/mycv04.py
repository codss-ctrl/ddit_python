import cv2
 
img = cv2.imread('lena.jpg',1)

#resize_img = cv2.resize(img, (200, 200))
#print("resize_img.shape = {0}".format(resize_img.shape))

img_resize = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_AREA)


cv2.imshow('Test Image', img_resize)
cv2.waitKey(0)

cv2.destroyAllWindows()
 
# 출력
# img.shape = (360, 480, 3)
# resize_img.shape = (300, 300, 3)



































