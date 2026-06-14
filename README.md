# 🏍️ Real-Time Helmet Detection System using YOLOv8

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Object%20Detection-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

# 🏍️ Real-Time Helmet Detection System using YOLOv8

## Overview

Road safety remains one of the most critical challenges in modern transportation systems. Among two-wheeler riders, failure to wear a helmet significantly increases the risk of severe head injuries and fatalities during accidents.

This project presents a real-time helmet detection system developed using the YOLOv8 object detection framework. The system automatically identifies whether a motorcycle rider is wearing a helmet or not from images and video streams. The goal is to demonstrate how deep learning and computer vision can assist traffic monitoring systems by automating helmet compliance detection.

The project was developed as part of a Minor Project in the Department of Electrical Engineering at Manipal University Jaipur.

---

## Problem Statement

Manual monitoring of helmet compliance is difficult in high-traffic environments. Traffic personnel cannot continuously observe every vehicle at every junction, leading to inconsistent enforcement of safety regulations.

The objective of this project is to develop an automated computer vision solution capable of:

* Detecting riders wearing helmets
* Detecting riders without helmets
* Processing images and video streams in real time
* Providing a scalable foundation for intelligent traffic monitoring systems

---

## Key Features

* Real-time helmet detection
* Detection of "With Helmet" and "Without Helmet" riders
* YOLOv8-based object detection framework
* Custom-trained deep learning model
* Video and image inference support
* Performance evaluation using industry-standard metrics
* Lightweight deployment pipeline using Python and OpenCV

---

## Technology Stack

### Programming Language

* Python

### Deep Learning Framework

* YOLOv8 (Ultralytics)

### Libraries Used

* OpenCV
* NumPy
* Matplotlib
* Ultralytics YOLO
* Pandas

### Development Environment

* Jupyter Notebook
* Google Colab
* VS Code

---

## Dataset

The model was trained using a custom helmet detection dataset containing annotated motorcycle rider images.

### Classes

1. With Helmet
2. Without Helmet

### Dataset Characteristics

* Custom annotated dataset
* Diverse rider viewpoints
* Real-world traffic scenarios
* Multiple lighting conditions
* Augmented training samples

The dataset was prepared in YOLO format and used for supervised object detection training.

---

## Project Workflow

### Step 1: Data Collection

Images containing motorcycle riders with and without helmets were collected and organized into separate categories.

### Step 2: Data Annotation

Bounding boxes were created around riders and helmet regions using annotation tools compatible with YOLO format.

### Step 3: Data Preprocessing

The dataset underwent preprocessing operations including:

* Image resizing
* Normalization
* Data augmentation
* Train-validation splitting

### Step 4: Model Training

The YOLOv8l model was trained on the custom dataset using transfer learning.

Training Configuration:

* Model: YOLOv8l
* Image Size: 640 × 640
* Optimizer: AdamW
* Epochs: 100

### Step 5: Model Evaluation

The trained model was evaluated using:

* Precision
* Recall
* F1 Score
* Average Precision (AP)
* Mean Average Precision (mAP)

### Step 6: Inference

The final model performs real-time detection on images and videos by generating bounding boxes around detected classes and displaying confidence scores.

---

## System Architecture

Input Image / Video

↓

Image Preprocessing

↓

YOLOv8 Detection Network

↓

Feature Extraction

↓

Object Classification

↓

Helmet / No Helmet Prediction

↓

Detection Visualization

---

## Performance Results

The trained model achieved the following results:

| Metric              | Value |
| ------------------- | ----- |
| AP (With Helmet)    | 0.877 |
| AP (Without Helmet) | 0.654 |
| mAP@0.5             | 0.765 |

The model demonstrated strong performance in identifying helmet usage under varying environmental conditions and traffic scenes.

---

## Challenges Encountered

### Class Imbalance

The dataset contained more helmet samples compared to no-helmet samples, which affected model learning.

### Occlusions

Partial visibility of riders and helmets occasionally reduced detection confidence.

### Complex Backgrounds

Traffic environments contain vehicles, pedestrians, and visual clutter that increase detection difficulty.

### Lighting Variations

Detection performance varied under shadows, low-light conditions, and strong sunlight.

---

## Results and Observations

The trained YOLOv8 model successfully learned discriminative features related to helmet usage and produced reliable detections on unseen images.

Key observations include:

* High precision for helmet detection
* Stable performance across different traffic scenarios
* Fast inference suitable for real-time applications
* Good generalization capability on validation data

The project demonstrates the effectiveness of modern object detection architectures for traffic safety applications.

---

## Applications

* Traffic surveillance systems
* Smart city monitoring
* Road safety awareness programs
* Automated compliance monitoring
* Educational and research purposes
* Computer vision learning projects

---

## Future Scope

The current project focuses exclusively on helmet detection.

Possible future enhancements include:

* Detection of two-wheelers and riders separately
* Rider-to-vehicle association logic
* Number plate detection
* Optical Character Recognition (OCR) integration
* Violation logging and reporting
* Edge-device deployment for real-time roadside monitoring

---

## Repository Structure

project/

├── docs/

├── models/

├── results/

├── src/

├── demo/

├── README.md

├── requirements.txt

└── LICENSE

---

## Author

Naman Bhasin



