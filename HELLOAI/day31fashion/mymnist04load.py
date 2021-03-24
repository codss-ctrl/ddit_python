import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images_ori, test_labels) = fashion_mnist.load_data()

img = cv2.imread('baji.jpg',cv2.IMREAD_COLOR)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_r = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA)

img2gmi = 255 - img_r

train_images, test_images = train_images / 255.0, test_images_ori / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

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
















    