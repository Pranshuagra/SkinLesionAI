from flask import Flask
from flask import render_template
from flask import request

from werkzeug.utils import secure_filename

from model.model_loader import load_model
from model.predictor import predict_image
from utils.charts import generate_pie_chart
import os
from utils.report_generator import (
    generate_pdf_report
)
from utils.report_generator import (
    generate_pdf_report,
    generate_batch_pdf_report
)
# ==================================================
# APP CONFIG
# ==================================================

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "uploads"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

os.makedirs(
    os.path.join(BASE_DIR, "static", "reports"),
    exist_ok=True
)

os.makedirs(
    os.path.join(BASE_DIR, "static", "charts"),
    exist_ok=True
)
# ==================================================
# LOAD MODEL ONCE
# ==================================================
print("APP STARTED")
model = load_model()

print("MODEL LOADED")
# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# ==================================================
# SINGLE IMAGE PREDICTION
# ==================================================

@app.route("/predict", methods=["POST"])
def predict():

    # ==========================
    # PATIENT DETAILS
    # ==========================

    patient_name = request.form.get(
        "patient_name"
    )

    patient_age = request.form.get(
        "patient_age"
    )

    # ==========================
    # IMAGE CHECK
    # ==========================

    if "image" not in request.files:

        return "No image uploaded"

    image = request.files["image"]

    if image.filename == "":

        return "No image selected"

    filename = secure_filename(
        image.filename
    )

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(filepath)

    # ==========================
    # MODEL PREDICTION
    # ==========================

   
    try:
        prediction, confidence = predict_image(
            filepath,model)
    except Exception as e:
        print("prediction error:", e)
        return render_template(
            "result.html",
            message="Invalid image uploaded. Please upload a valid skin lesion image.")
    
    

    # ==========================
    # RISK LEVEL
    # ==========================

    if prediction == "Malignant":

        risk_level = "High Risk"

    else:

        risk_level = "Low Risk"
    pdf_path = generate_pdf_report(
    patient_name,
    patient_age,
    prediction,
    confidence,
    risk_level
)
    
    # ==========================
    # RESULT PAGE
    # ==========================

    return render_template(
        "result.html",
        image_path=filepath,
        prediction=prediction,
        confidence=f"{confidence}%",
        risk_level=risk_level,
        patient_name=patient_name,
        patient_age=patient_age,pdf_path=pdf_path
    )

# ==================================================
# MULTIPLE IMAGE PREDICTION
# ==================================================

@app.route("/batch_predict", methods=["POST"])
def batch_predict():

    images = request.files.getlist("images")

    results = []

    benign_count = 0
    malignant_count = 0

    for image in images:

        if image.filename == "":
            continue

        filename = secure_filename(
            image.filename
        )

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        image.save(filepath)

        
        
        try:
            prediction, confidence = predict_image(
                filepath,
                model
            )
        except Exception as e:
            print("prediction error:", e)
            continue

        if prediction == "Benign":
            benign_count += 1
            risk_level = "Low Risk"

        else:
            malignant_count += 1
            risk_level = "High Risk"

        results.append({

            "filename": filename,
            "prediction": prediction,
            "confidence": confidence,
            "risk_level": risk_level

        })

    total_images = len(results)

    # AI Observation
    if malignant_count > 0:

        observation = (
            "One or more uploaded skin lesion images show "
            "characteristics associated with malignant lesions. "
            "Further dermatological evaluation is recommended."
        )

    else:

        observation = (
            "All uploaded images appear benign based on "
            "the trained deep learning model."
        )

    # PDF Generate
    pdf_path = generate_batch_pdf_report(
        results,
        total_images,
        benign_count,
        malignant_count
    )
    chart_path = generate_pie_chart(
    benign_count,
    malignant_count)

    return render_template(
        "batch_result.html",
        results=results,
        total_images=total_images,
        benign_count=benign_count,
        malignant_count=malignant_count,
        observation=observation,chart_path=chart_path,
        pdf_path=pdf_path
    )

# ==================================================
# RUN APP
# ==================================================

import os

if __name__ == "__main__":
    port = int(
        os.environ.get(
            "PORT",
            7860
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )