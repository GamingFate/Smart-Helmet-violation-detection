# 💻 Source Code

This directory contains the implementation files used for training, inference, and experimentation of the YOLOv8-based Helmet Detection System.

---

## 📁 Files

| File                        | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| `helmet_detection_image.py` | Performs helmet detection on input images using the trained YOLOv8 model  |
| `helmet_detection_video.py` | Performs real-time helmet detection on video streams                      |
| `Helmet_Detection.ipynb`    | Jupyter Notebook used for experimentation, training, and model evaluation |

---

## 🖼️ Image Detection

The image detection script loads the trained YOLOv8 model and performs object detection on a single image.

### Features

* Helmet and no-helmet classification
* Bounding box visualization
* Confidence score display
* OpenCV-based output rendering

---

## 🎥 Video Detection

The video detection script performs frame-by-frame helmet detection on video input.

### Features

* Real-time inference
* GPU acceleration using CUDA
* Bounding box visualization
* Confidence score display
* Support for recorded traffic footage

---

## 🧠 Model

All inference scripts utilize a custom-trained YOLOv8l model trained on an annotated helmet detection dataset.

Classes:

* With Helmet
* Without Helmet

---

## 🚀 Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* PyTorch
* CVZone
* Jupyter Notebook

---

## Purpose

These scripts demonstrate the complete inference pipeline used in the project and provide examples of applying computer vision techniques for automated helmet detection and road safety monitoring.
