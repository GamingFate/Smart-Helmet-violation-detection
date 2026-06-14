# 🏍️ Real-Time Helmet Detection System using YOLOv8

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Object%20Detection-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

Road safety remains one of the most critical challenges in modern transportation systems. Among two-wheeler riders, failure to wear a helmet significantly increases the risk of severe head injuries and fatalities during accidents.

This project presents a **real-time helmet detection system** developed using the YOLOv8 object detection framework. The system automatically identifies whether a rider is wearing a helmet or not from images and video streams.

The project was developed as part of a **Minor Project** in the Department of Electrical Engineering at **Manipal University Jaipur**.

---

## 🚀 Key Highlights

* Custom-trained YOLOv8l model
* Real-time image and video inference
* Helmet and no-helmet classification
* GPU-accelerated detection using PyTorch
* Trained on a custom annotated dataset
* mAP@0.5 of **76.5%**
* AP of **87.7%** for Helmet Detection
* Comprehensive evaluation using Precision, Recall, F1 Score, and mAP metrics

---

## 🎯 Problem Statement

Manual monitoring of helmet compliance is difficult in high-traffic environments. Traffic personnel cannot continuously observe every vehicle at every junction, leading to inconsistent enforcement of safety regulations.

The objective of this project is to develop an automated computer vision solution capable of:

* Detecting riders wearing helmets
* Detecting riders without helmets
* Processing images and video streams in real time
* Demonstrating practical applications of deep learning in traffic safety monitoring

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Deep Learning Framework

* YOLOv8 (Ultralytics)

### Libraries Used

* OpenCV
* PyTorch
* NumPy
* Pandas
* Matplotlib
* CVZone

### Development Tools

* Google Colab
* Jupyter Notebook
* VS Code

---

## 📂 Dataset

The model was trained using a custom helmet detection dataset containing annotated rider images.

### Classes

| Class ID | Class Name     |
| -------- | -------------- |
| 0        | With Helmet    |
| 1        | Without Helmet |

### Dataset Features

* Custom annotations
* Real-world traffic imagery
* Multiple viewpoints
* Diverse rider appearances
* Various lighting conditions
* YOLO format annotations

---

## ⚙️ Project Workflow

### 1. Data Collection

Images containing riders with and without helmets were collected and organized into separate categories.

### 2. Data Annotation

Bounding boxes were created around target objects using YOLO-compatible annotation tools.

### 3. Data Preprocessing

* Image resizing
* Normalization
* Data augmentation
* Train-validation split

### 4. Model Training

The YOLOv8l model was trained using transfer learning.

#### Training Configuration

| Parameter  | Value     |
| ---------- | --------- |
| Model      | YOLOv8l   |
| Epochs     | 100       |
| Image Size | 640 × 640 |
| Optimizer  | AdamW     |

### 5. Evaluation

The trained model was evaluated using:

* Precision
* Recall
* F1 Score
* Average Precision (AP)
* Mean Average Precision (mAP)

### 6. Inference

The final model performs real-time detection on images and videos while displaying class labels, confidence scores, and bounding boxes.

---

## 🧠 System Architecture

```text
Input Image / Video
          │
          ▼
   Preprocessing
          │
          ▼
      YOLOv8l
          │
          ▼
 Feature Extraction
          │
          ▼
 Classification
          │
          ▼
 Helmet / No Helmet
          │
          ▼
 Detection Output
```

---

## 📊 Performance Results

| Metric              | Score |
| ------------------- | ----- |
| AP (With Helmet)    | 0.877 |
| AP (Without Helmet) | 0.654 |
| mAP@0.5             | 0.765 |

The model demonstrated strong performance in identifying helmet usage under varying environmental conditions and traffic scenarios.

For detailed evaluation metrics, confusion matrices, training curves, and prediction examples, please refer to the **results** directory.

---

## 🔍 Challenges Encountered

### Class Imbalance

The dataset contained more helmet samples than no-helmet samples, affecting class distribution.

### Occlusions

Partial visibility of riders and helmets occasionally reduced detection confidence.

### Complex Backgrounds

Traffic environments contain visual clutter, vehicles, and pedestrians that increase detection difficulty.

### Lighting Variations

Detection performance varied under shadows, low-light conditions, and strong sunlight.

---

## 💡 Applications

* Traffic surveillance systems
* Road safety awareness programs
* Smart city monitoring
* Automated compliance monitoring
* Educational and research projects
* Computer vision learning applications

---

## 🔮 Future Scope

The current implementation focuses exclusively on helmet detection.

Potential future enhancements include:

* Two-wheeler detection
* Rider-to-vehicle association
* Number plate detection
* OCR-based number plate recognition
* Violation logging system
* Edge-device deployment

---

## 📁 Repository Structure

```text
Smart-Helmet-violation-detection/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── helmet_detection_image.py
│   ├── helmet_detection_video.py
│   ├── Helmet_Detection.ipynb
│   └── README.md
│
└── results/
    ├── README.md
    ├── evaluation metrics
    ├── training visualizations
    ├── confusion matrices
    └── prediction samples
```

---

## 👨‍💻 Author

**Naman Bhasin**



---

## 📜 License

This project is licensed under the MIT License.
