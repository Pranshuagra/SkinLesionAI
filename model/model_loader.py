# model/model_loader.py

import torch
import torch.nn as nn

from torchvision import models

MODEL_PATH = r"model\best_resnet18_skin_lesion.pth"

device = torch.device("cpu")

def load_model():

    model = models.resnet18(weights=None)

    model.fc = nn.Linear(
        model.fc.in_features,
        2
    )

    model.load_state_dict(
        torch.load(
            MODEL_PATH,
            map_location=device
        )
    )

    model.eval()

    return model