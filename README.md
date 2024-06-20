# GIF<br>

![dd](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/ce96d3b1-0901-4611-b391-d332b958f5df)

<br>
<br>
<br>
<br>

# Project Overview

This project aims to create a web application for letter recognition using Convolutional Neural Networks (CNNs) with JavaScript and Flask.

# Description
The "CNN Letter Recognition with JS Flask" project combines frontend and backend technologies to deliver a web-based letter recognition system. Here's a breakdown of its components:

#### Frontend (JavaScript)
Interactive user interface developed with JavaScript.
Allows users to upload images containing letters for recognition.

#### Backend (Flask)
Utilizes Flask, a Python web framework, for backend processing.
Handles image processing tasks and interfaces with the CNN model.

#### Convolutional Neural Networks (CNNs)
Trained CNN model for letter recognition.
Predicts letters present in input images.


<br>
<br>

### Used Technologies
- Tensorflow
- Keras
- Numpy
- Panda
- OpenCV
- Python
- JavaScript
- Flask
- HTML
- CSS

<br>

# CNN Model
This section describes the implementation of the Convolutional Neural Network (CNN) model for letter recognition in the project. Below are the steps involved:

### Data Preprocessing
The dataset is loaded from the CSV file containing handwritten letters in pixel values.
Data types are converted to 'float32' for compatibility with TensorFlow.

### Exploratory Data Analysis (EDA)
Initial analysis of the dataset is performed using the data.head() and data.describe() methods to understand its structure and distribution.

###  Data Splitting
The dataset is split into features (X) and labels (y), where X contains pixel values of images and y contains corresponding labels.

###  Normalization
Pixel values in X are normalized by dividing them by 255.0 to scale them between 0 and 1.

###  Data Augmentation
Data augmentation is applied to increase the diversity of the dataset, improving model generalization.
Augmentation techniques include rotation, width and height shifting, zooming, shearing, and horizontal flipping.
<br>

![ttt](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/4ede5dfc-f2e5-40c7-8eb4-044bc8cbb502)
<br>

###  Model Architecture
A Sequential model is initialized to build the CNN architecture.
Three convolutional layers with 64 filters each and ReLU activation are added, followed by max-pooling layers.
The Flatten layer is added to convert the 2D feature maps into a 1D vector.
Dropout is applied to mitigate overfitting.
Dense layers with ReLU activation are added, followed by a final Dense layer with softmax activation for classification.

<br>

![qq](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/21d2a48b-d594-4676-9878-e3fe5686737b)
<br>

###  Model Compilation
The model is compiled using the Adam optimizer with a learning rate of 0.001 and categorical cross-entropy loss function.
Accuracy is chosen as the evaluation metric.

###  Model Training
The augmented data is fed into the model for training using the fit() method.
Early stopping and model checkpointing callbacks are applied to prevent overfitting and save the best model.

###  Model Evaluation
The model is evaluated on the test dataset using the evaluate() method to obtain loss and accuracy metrics.
Test accuracy and loss are printed to assess model performance.

<br>

![acc](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/2529e307-f0b2-480b-8ab5-2de56bfe9849)
<br>
<br>

### Model Summary
![summary](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/da9471f0-1acb-4413-94c3-223ec243a3ca)



