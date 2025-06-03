from PIL import Image
import numpy as np
import os
import math

FOLDER = "baroque_paintings"
THRESHOLD_ENTROPY = 4.5  # da testare: 5+ è molto dettagliato

def calculate_entropy(img):
    grayscale = img.convert("L")  # grayscale
    histogram = grayscale.histogram()
    histogram_length = sum(histogram)
    samples_probability = [float(h) / histogram_length for h in histogram]
    entropy = -sum([p * math.log2(p) for p in samples_probability if p != 0])
    return entropy

for file in os.listdir(FOLDER):
    if not (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg") or file.lower().endswith(".png")):
        continue

    path = os.path.join(FOLDER, file)
    try:
        with Image.open(path) as img:
            entropy = calculate_entropy(img)
            if entropy < THRESHOLD_ENTROPY:
                print(f"[⚠️] Scarsa qualità ({entropy:.2f}): {file}")
                os.remove(path)
            else:
                print(f"[✅] OK ({entropy:.2f}): {file}")
    except Exception as e:
        print(f"[💥] Errore su {file}: {e}")

