# Fassion_MNIST_Classification
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This repository consists of different classification models trained on the Fassion Mnist data set.
____

## ABOUT THE DATA SET
The images and labels used to train all the models in the repositary was loaded directly from KERAS using the below command
```sh
# To load data
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.fassion_mnist.load_data()
```
The train data has 60000 samples and the test data has 10000 samples which sums up to a total of 70000 samples.
Each image has a resolution of 28X28 which gives us 784 pixels when flattened.

There are a total number of 10 classes of images and every image has its label.

## CLASSIFICATION MODELS
Four machine_learning models and three deep_learning models were trained out of which the custom designed cnn model named CNN2 gave the best results. Below are the resuls of different models.

| MODEL_NAME  | ACCURACY | CODE | 
| ------------- | ------------- | ------------- |
| ANN1 | 0.9758999943733215  | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/ANN_1/Fashion_MNIST_ANN.ipynb) |
| CNN2  | 0.9008 | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/CNN2/Fassion_mnist_cnn2.ipynb) |
| CNN1 | 0.8882 | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/CNN1/Fassion_MNIST1_CNN.ipynb) |
| Random_Forest | 0.88 | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/Random%20forest/Fashion_MNIST_RFC.ipynb) |
| K_Nearest_Neighbor | 0.86 | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/KNN/Fashion_MNIST_KNN.ipynb) |
| Support_Vector_Machines | 0.8402 | [🔗](https://github.com/VIKNESH1211/Fassion_MNIST_Classification/blob/main/Support%20Vector%20Machines/Fassion_MNIST_classifiers.ipynb) |
