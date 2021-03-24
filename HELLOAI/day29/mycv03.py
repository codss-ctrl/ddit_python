import cv2
import numpy as np
 
# 이미지 읽기
img = cv2.imread('3_4.png',cv2.IMREAD_COLOR)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img_g)
# 이미지 화면에 표시
cv2.imshow('Test Image', img_g)
cv2.waitKey(0)



































