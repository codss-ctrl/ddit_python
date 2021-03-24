import tensorflow as tf
import cv2

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for i in range(100):
    cv2.imwrite("train/"+str(train_labels[i])+"_"+str(i)+".jpg", train_images[i])
    

train_images, test_images = train_images / 255.0, test_images / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)


cv2.waitKey(0)
cv2.destroyAllWindows()
















    