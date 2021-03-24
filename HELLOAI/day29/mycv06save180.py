import cv2
 
img = cv2.imread('lena.jpg',1)


img_resize = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_AREA)


img180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('Test Image', img180)
cv2.waitKey(0)

cv2.destroyAllWindows()
 
cv2.imwrite("lena_180.jpeg", img180)




































