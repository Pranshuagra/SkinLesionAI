import matplotlib.pyplot as plt
import os


def generate_pie_chart(
    benign_count,
    malignant_count
):

    labels = [
        "Benign",
        "Malignant"
    ]

    sizes = [
        benign_count,
        malignant_count
    ]

    plt.figure(figsize=(5, 5))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Skin Lesion Analysis Summary"
    )

    chart_path = os.path.join(
        "static",
        "images",
        "pie_chart.png"
    )

    plt.savefig(chart_path)

    plt.close()

    return chart_path