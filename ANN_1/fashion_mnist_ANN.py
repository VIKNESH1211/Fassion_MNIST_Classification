# -*- coding: utf-8 -*-
"""Fashion_MNIST2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16hspc3cZcdg_MQ6GXSTVTuZkEz68juZh
"""

import tensorflow as tf 
from tensorflow import keras
import matplotlib.pyplot as plt 
import numpy as np

(x_train,y_train),(x_test,y_test)= tf.keras.datasets.fashion_mnist.load_data()

import sklearn
from sklearn.model_selection import train_test_split

x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,test_size=0.10,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(x_val.shape)
print(y_train.shape)
print(y_test.shape)
print(y_val.shape)

x_train  = x_train.reshape(54000,28,28,1)
x_test  = x_test.reshape(10000,28,28,1)
x_val  = x_val.reshape(6000,28,28,1)

print(x_train.shape)
print(x_test.shape)
print(x_val.shape)
print(y_train.shape)
print(y_test.shape)
print(y_val.shape)

label = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle-boot']

print(x_train[3].min())
print(x_train[3].max())

x_train = x_train/255
x_test = x_test/255
x_val = x_val/255

print(x_train[3].min())
print(x_train[3].max())

[x_train][0].shape

y_train[0].shape

"""MODEL"""

model2 = tf.keras.models.Sequential()

#rules to define neurons for the hidden layer
# neurons between 10 and 784
# (2/3*784)+10 = 532


model2.add(keras.layers.Flatten(input_shape = x_train[0].shape))
model2.add(keras.layers.Dense(532 , activation = 'relu'))
model2.add(keras.layers.Dense(10 , activation = 'Softmax'))

model2.compile(optimizer = 'SGD', loss = tf.keras.losses.SparseCategoricalCrossentropy() , metrics = ['accuracy'])

history = model2.fit(x_test,y_test , validation_data = (x_val,y_val) , epochs = 20)

print(model2.evaluate(x_test,y_test , verbose = '1'))

model2.save("model2.hdf5")

import matplotlib.pyplot as plt


def plot_hist(hist):
    plt.plot(hist.history["loss"])
    plt.plot(hist.history["val_loss"])
    plt.title("loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()

plot_hist(history)
