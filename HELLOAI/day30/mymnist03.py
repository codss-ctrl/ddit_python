# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2
import numpy as np


# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print("google",test_labels[0])


# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))#넘피 구조 바꿈
train_images = train_images.astype('float32') / 255
test_images_sec = test_images.reshape((10000, 28 * 28))
test_images_sec = test_images_sec.astype('float32') / 255

# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels_sec = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)
predictions = model.predict(test_images_sec)

        
print("predict",np.argmax(predictions[0]))
print("google",test_labels[0])

ok_cnt=0
ng_cnt=0

for i in range(len(predictions)):
    pred = np.argmax(predictions[i])
    goog = test_labels[i] 
    if pred == goog:
       ok_cnt +=1
    else :
       ng_cnt +=1 
       cv2.imwrite("miss/"+str(goog)+"_"+str(pred)+"_"+str(i)+".jpg",test_images[i])                              

print("ok_cnt",ok_cnt)
print("ng_cnt",ng_cnt)

cv2.waitKey(0)
cv2.destroyAllWindows()

test_loss, test_acc = model.evaluate(test_images_sec, test_labels_sec)
print('test_acc: ', test_acc)


