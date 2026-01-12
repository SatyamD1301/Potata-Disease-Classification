# Potata-Disease-Classification
Potato Disease Classification is a deep learning project that detects diseases in potato leaves using image analysis. A CNN model classifies images into Healthy, Early Blight, and Late Blight. It enables early disease detection, helping farmers reduce crop loss and improve productivity.
# Objectives

. Detect potato leaf diseases accurately using AI

. Classify leaf images into Healthy, Early Blight, and Late Blight

. Reduce crop loss through early detection

. Provide a fast and automated disease detection system

# Model Description

. The project uses a CNN (Convolutional Neural Network) trained on potato leaf images.
. The model automatically learns visual patterns such as spots, discoloration, and texture differences that indicate diseases.

 # CNN Workflow:

. Image preprocessing (resize, normalization)

. Feature extraction using convolution layers

. Downsampling using max pooling

. Classification using fully connected layers

# Dataset

. Potato leaf images dataset

. Three classes:

. Healthy

. Early Blight

. Late Blight

. Images are preprocessed before training to improve model performance.

# Tech Stack

. Python

. TensorFlow

. Keras

. Convolutional Neural Network (CNN)

. FastAPI (Backend API)

. TensorFlow Serving (Model deployment)

. React.js (Frontend – optional)

# Project Workflow

. User uploads a potato leaf image

. Image is sent to FastAPI backend

. Image is preprocessed

. CNN model predicts the disease

. Result is returned to the user

# Features

. AI-based disease detection

. Fast and accurate predictions

. REST API support

. Easy integration with frontend

. Supports smart agriculture

# Use Case

. This project can be used by farmers and agricultural experts to detect potato diseases at an early stage, helping reduce crop damage and improve productivity.

# Future Enhancements

. Support for more crop diseases

. Mobile application integration

. Real-time camera detection

. Cloud deployment
