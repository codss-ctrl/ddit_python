import cv2
import numpy as np
 
img = cv2.imread('baji.jpg',cv2.IMREAD_COLOR)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_r = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA)

img2gmi = 255 - img_r

img_out = np.reshape(img2gmi,(1,28,28))

print(img_out.shape)

cv2.imshow('baji', img2gmi)
cv2.waitKey(0)
cv2.destroyAllWindows()


































