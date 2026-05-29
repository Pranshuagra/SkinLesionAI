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

## 📌 Overview

SkinLesionAI is an intelligent healthcare application that uses Deep Learning and Computer Vision techniques to classify skin lesion images into **Benign** and **Malignant** categories.

The system allows users to upload single or multiple dermoscopic images and receive automated predictions, confidence scores, risk assessments, AI observations, PDF reports, and visual analytics.

---

## 🚀 Features

* ✅ Single Image Prediction
* ✅ Multiple Image Analysis
* ✅ Benign vs Malignant Classification
* ✅ Deep Learning using ResNet18
* ✅ Confidence Score Calculation
* ✅ Risk Level Assessment
* ✅ AI-Based Medical Observation
* ✅ Patient Name & Age Input
* ✅ PDF Report Generation
* ✅ Batch PDF Report Export
* ✅ Pie Chart Analytics
* ✅ Invalid Image Handling
* ✅ Flask-Based Interactive UI

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

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SkinLesionAI.git
```

### Move to Project Directory

```bash
cd SkinLesionAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 🌐 Deployment

This project can be deployed on:

* Render
* Railway
* Hugging Face Spaces
* AWS EC2
* Azure App Service

### Render Deployment

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
gunicorn app:app
```

---

## 📊 Future Enhancements

* Camera Capture Support
* CSV Export
* Prediction History Dashboard
* Explainable AI (Grad-CAM)
* Doctor Recommendation System
* Multi-Class Skin Disease Detection
* Cloud Database Integration

---

## 👨‍💻 Author

### Pranshu Agrahari

Data Analyst | Machine Learning Enthusiast | AI Developer

**Skills**

* Python
* Flask
* Machine Learning
* Deep Learning
* Power BI
* Data Analytics


---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

<div align="center">

### Made with ❤️ using Flask, PyTorch and Deep Learning

</div>
