import cv2
import os
import shutil

FOLDER = "baroque_paintings"
OUTPUT_FOLDER = "selected_paintings"
THRESHOLD = 100.0  # Soglia da regolare

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def laplacian_variance(image_path):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f"Immagine non caricata: {image_path}")
            return 0
        laplacian = cv2.Laplacian(image, cv2.CV_64F)
        variance = laplacian.var()
        print(f"{os.path.basename(image_path)}: varianza Laplaciana = {variance:.2f}")
        return variance
    except Exception as e:
        print(f"Errore con {image_path}: {e}")
        return 0

def main():
    for filename in os.listdir(FOLDER):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(FOLDER, filename)
            score = laplacian_variance(path)
            if score < THRESHOLD:
                print(f"Scartata per bassa qualità: {filename} ({score:.2f})")
            else:
                print(f"OK: {filename} ({score:.2f})")
                shutil.copy(path, os.path.join(OUTPUT_FOLDER, filename))

if __name__ == "__main__":
    main()
