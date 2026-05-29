from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_pdf_report(
    patient_name,
    patient_age,
    prediction,
    confidence,
    risk_level
):

    os.makedirs("static/reports", exist_ok=True)

    pdf_path = os.path.join(
        "static",
        "reports",
        "report.pdf"
    )

    c = canvas.Canvas(pdf_path)

    c.drawString(
        100,
        800,
        "Skin Lesion Analysis Report"
    )

    c.drawString(
        50,
        760,
        f"Patient Name: {patient_name}"
    )

    c.drawString(
        50,
        740,
        f"Patient Age: {patient_age}"
    )

    c.drawString(
        50,
        720,
        f"Prediction: {prediction}"
    )

    c.drawString(
        50,
        700,
        f"Confidence: {confidence}"
    )

    c.drawString(
        50,
        680,
        f"Risk Level: {risk_level}"
    )

    c.drawString(
        50,
        650,
        f"Generated On: {datetime.now()}"
    )

    c.save()

    return pdf_path


def generate_batch_pdf_report(
    results,
    total_images,
    benign_count,
    malignant_count
):

    os.makedirs(
        "static/reports",
        exist_ok=True
    )

    pdf_path = os.path.join(
        "static",
        "reports",
        "batch_report.pdf"
    )

    c = canvas.Canvas(pdf_path)

    c.drawString(
        100,
        800,
        "Batch Skin Lesion Analysis Report"
    )

    c.drawString(
        50,
        760,
        f"Total Images: {total_images}"
    )

    c.drawString(
        50,
        740,
        f"Benign Cases: {benign_count}"
    )

    c.drawString(
        50,
        720,
        f"Malignant Cases: {malignant_count}"
    )

    y = 680

    for item in results:

        filename = item["filename"][:30]

        c.drawString(
            50,
            y,
            filename
        )

        c.drawString(
            300,
            y,
            item["prediction"]
        )

        c.drawString(
            420,
            y,
            str(item["confidence"])
        )

        y -= 20

    # PIE CHART

    chart_path = os.path.join(
        "static",
        "images",
        "pie_chart.png"
    )

    if os.path.exists(chart_path):

        c.drawImage(
            chart_path,
            120,
            350,
            width=300,
            height=220
        )

    c.drawString(
        50,
        80,
        f"Generated On: {datetime.now()}"
    )

    c.save()

    return pdf_path