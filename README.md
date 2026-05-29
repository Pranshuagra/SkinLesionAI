# 🩺 SkinLesionAI

<div align="center">

### Deep Learning-Based Skin Lesion Classification System

Detect Benign and Malignant Skin Lesions using ResNet18 and Flask

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

## 🎥 Demo

<p align="center">

<img src="assets/demo.gif" width="900">

</p>

> Replace the GIF above with your project demo recording.

---



## 📌 Project Overview

SkinLesionAI is a web-based healthcare application developed to assist in the preliminary analysis of skin lesion images using Deep Learning. The system utilizes a fine-tuned ResNet18 model trained on skin lesion datasets to classify images into two categories: **Benign** and **Malignant**.

The application provides a user-friendly interface where users can upload either a single skin lesion image or multiple images simultaneously for analysis. After processing the uploaded images, the model generates predictions along with confidence scores and risk assessments. To improve usability, the system automatically creates detailed PDF reports containing patient information, prediction results, confidence levels, and medical observations.

For batch analysis, the application generates summary statistics and visual analytics in the form of pie charts, allowing users to quickly understand the distribution of benign and malignant cases among uploaded images. The system also includes error handling mechanisms to prevent failures when unsupported or corrupted images are uploaded.

The primary objective of this project is to demonstrate the practical application of Deep Learning in medical image analysis while providing an easy-to-use platform that combines image classification, automated reporting, and healthcare-oriented visualization within a single Flask-based web application.

This project was developed using Python, Flask, PyTorch, ReportLab, and Matplotlib, integrating machine learning and web technologies to create an end-to-end intelligent diagnostic support system.


---

🚀 Key Features
Deep Learning-based skin lesion classification using a trained ResNet18 model.
Single image prediction with confidence score generation.
Multiple image batch analysis for simultaneous lesion evaluation.
Automatic classification into Benign and Malignant categories.
Risk level assessment based on prediction results.
AI-generated medical observation summaries.
Patient information management including name and age.
Automatic PDF report generation for individual predictions.
Batch PDF report generation for multiple image analyses.
Pie chart visualization showing lesion distribution.
Secure image upload and validation mechanisms.
Flask-based responsive web interface for easy accessibility.

---

## 🧠 Deep Learning Model

| Parameter         | Details           |
| ----------------- | ----------------- |
| Model             | ResNet18          |
| Framework         | PyTorch           |
| Input Size        | 224 × 224         |
| Classes           | Benign, Malignant |
| Transfer Learning | Yes               |
| Optimizer         | Adam              |
| Loss Function     | CrossEntropyLoss  |

---

## 🏗 System Architecture

```text
User Upload
     │
     ▼
Flask Web Application
     │
     ▼
Image Preprocessing
     │
     ▼
ResNet18 Model
     │
     ▼
Prediction Engine
     │
     ├── Confidence Score
     ├── Risk Level
     ├── AI Observation
     ├── PDF Report
     └── Analytics
```

---

## 📂 Project Structure

```text
SkinLesionAI/

│
├── app.py
│
├── model/
│   ├── model_loader.py
│   ├── predictor.py
│   └── isic_resnet18_model.pth
│
├── static/
│   ├── uploads/
│   ├── reports/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── batch_result.html
│   └── error.html
│
├── utils/
│   ├── report_generator.py
│   └── charts.py
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## 📸 Screenshots

### Home Page

![Home Page](assets/home.png)

### Single Image Prediction

![Single Prediction](assets/single_prediction.png)

### Batch Prediction

![Batch Prediction](assets/batch_prediction.png)

### PDF Report

![PDF Report](assets/pdf_report.png)

### Analytics Dashboard

![Analytics](assets/chart.png)

---

## 📄 Reports Generated

The application automatically generates:

* Individual Patient PDF Reports
* Batch Analysis PDF Reports
* Risk Assessment Reports
* Prediction Summaries
* Pie Chart Analytics

---



## 📊 Future Enhancements

* Camera Capture Support
* CSV Export
* Prediction History Dashboard
* Explainable AI (Grad-CAM)
* Doctor Recommendation System
* Multi-Class Skin Disease Detection
* Cloud Database Integration


## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

