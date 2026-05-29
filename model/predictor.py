# model/predictor.py

import torch
from PIL import Image
from torchvision import transforms

# ==================================================
# CLASS NAMES
# ==================================================

CLASS_NAMES = [
    "Benign",
    "Malignant"
]

# ==================================================
# IMAGE TRANSFORM
# ==================================================

transform = transforms.Compose([

    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )

])

# ==================================================
# PREDICTION FUNCTION
# ==================================================

def predict_image(image_path, model):

    image = Image.open(
        image_path
    ).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probs = torch.softmax(
            outputs,
            dim=1
        )

        confidence, pred = torch.max(
            probs,
            1
        )

        # ==================================
        # DEBUGGING OUTPUT
        # ==================================

        print("\n" + "=" * 60)

        print("Raw Outputs:")
        print(outputs)

        print("\nProbabilities:")
        print(probs)

        print("\nPredicted Index:")
        print(pred.item())

        print("\nConfidence:")
        print(confidence.item())

        print("=" * 60 + "\n")

    prediction = CLASS_NAMES[
        pred.item()
    ]

    confidence = round(
        confidence.item() * 100,
        2
    )

    return prediction, confidence