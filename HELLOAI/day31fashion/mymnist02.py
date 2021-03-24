import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images_ori, test_labels) = fashion_mnist.load_data()


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

predictions = model.predict(train_images)
print(np.argmax(predictions[0]))
print(test_labels[0])

ok_cnt=0
ng_cnt=0

for i in range(len(predictions)):
    pred = np.argmax(predictions[i])
    goog = test_labels[i] 
    if pred == goog:
       ok_cnt +=1
    else :
       ng_cnt +=1 
       cv2.imwrite("miss/"+str(goog)+"_"+str(pred)+"_"+str(i)+".jpg",test_images_ori[i])         

print("ok_cnt",ok_cnt)
print("ng_cnt",ng_cnt)

cv2.waitKey(0)
cv2.destroyAllWindows()
















    