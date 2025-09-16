import requests
import os
import urllib.parse
import json

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
    CATEGORY_NAME = config.get("CATEGORY_NAME", "Paintings by Jan van Goyen")
else:
    CATEGORY_NAME = "Paintings by Jan van Goyen"
    
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

CATEGORY_NAME = config.get("CATEGORY_NAME", "Paintings by Jan van Goyen")
SAVE_FOLDER = "baroque_paintings"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def get_images_from_category(category, limit=50):
    images = []
    url = "https://commons.wikimedia.org/w/api.php"

    params = {
        "action": "query",
        "generator": "categorymembers",
        "gcmtitle": f"Category:{CATEGORY_NAME}",
        "gcmtype": "file",
        "gcmlimit": "500",
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "query" in data:
        for pageid in data['query']['pages']:
            page = data['query']['pages'][pageid]
            try:
                info = page['imageinfo'][0]
                width = info.get('width', 0)
                height = info.get('height', 0)

                if width >= 1000 and height >= 800:
                    images.append(info['url'])
                else:
                    print(f"[⚠️] Scartata: {page['title']} ({width}x{height})")

            except KeyError:
                continue
    return images
def download_image(url, folder):
    filename = urllib.parse.unquote(url.split("/")[-1])
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        print(f"[🟡] Già scaricata: {filename}")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://commons.wikimedia.org/"
    }

    print(f"[🟢] Scarico: {filename}")
    try:
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=15)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
        else:
            print(f"[🔴] Errore download {filename} (status {r.status_code})")
    except Exception as e:
        print(f"[💥] Eccezione per {filename}: {e}")
def main():
    print("[🔍] Cerco immagini tramite API...")
    images = get_images_from_category(CATEGORY_NAME, limit=50)

    print(f"[📦] Trovate {len(images)} immagini da scaricare.")
    for url in images:
        download_image(url, SAVE_FOLDER)

if __name__ == "__main__":
    main()
