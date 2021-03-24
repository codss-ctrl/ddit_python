import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('my_fashion')

img = cv2.imread('baji.jpg',cv2.IMREAD_COLOR)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_r = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA)
img2gmi = 255 - img_r
img_out = np.reshape(img2gmi,(1,28,28))

predictions = model.predict(img_out)

print(predictions)
print("predict",np.argmax(predictions[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()
















    