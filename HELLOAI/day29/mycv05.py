import cv2
 
img = cv2.imread('lena.jpg',1)

#resize_img = cv2.resize(img, (200, 200))
#print("resize_img.shape = {0}".format(resize_img.shape))

img_resize = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_AREA)

# height, width = img_resize.shape[:2]
# M1 = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1) 
# M2 = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
# img_rotation = cv2.warpAffine(img_resize, M2, (width, height))

print(cv2.ROTATE_180)
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Test Image', img90)
cv2.waitKey(0)

cv2.destroyAllWindows()
 
# 출력
# img.shape = (360, 480, 3)
# resize_img.shape = (300, 300, 3)



































