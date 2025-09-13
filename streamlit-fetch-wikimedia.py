import streamlit as st
import os
import shutil
import json
import sys
import subprocess
from collections import deque

from fetch_wikimedia.scripts.fetch_dipinti import main as fetch_images
from fetch_wikimedia.scripts.filtro_entropia import main as entropy_filter
from fetch_wikimedia.scripts.filtro_laplaciano import main as laplace_filter


st.set_page_config(page_title="Wikimedia Art Filter", layout="centered")
    
st.title("🎨 Wikimedia Art Filter")
st.write("Scarica, filtra per qualità, e seleziona le immagini migliori.")

user_category = st.text_input("🎯 Categoria Wikimedia:", "Paintings by Jan van Goyen")

if st.button("🔄 Aggiorna categoria"):
    config_path = os.path.join("fetch_wikimedia", "scripts", "config.json")
    try:
        with open(config_path, "w") as f:
            json.dump({"CATEGORY_NAME": user_category}, f)
        st.success(f"✅ Categoria aggiornata a: {user_category}")
    except Exception as e:
        st.error(f"❌ Errore durante l'aggiornamento: {e}")
        
if st.button("🔍 Scarica immagini"):
    st.write("Inizio download...")
    log_box = st.empty()

    process = subprocess.Popen(
        [sys.executable, "fetch_wikimedia/scripts/fetch_dipinti.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    last_lines = deque(maxlen=5)  # 🔁 Solo le ultime 5 righe

    for line in process.stdout:
        last_lines.append(line)
        log_box.code("".join(last_lines))  # 🎯 Mostra solo le ultime 5

    process.wait()

    if process.returncode == 0:
        st.success("✅ Download completato!")
    else:
        st.error("❌ Qualcosa è andato storto!")
        
if st.button("🧠 Filtro entropia"):
    st.write("Filtraggio entropico in corso...")
    entropy_filter()
    st.success("Filtro entropia completato!")

if st.button("🌀 Filtro Laplaciano"):
    st.write("Analisi del dettaglio in corso...")
    laplace_filter()
    st.success("Filtro Laplaciano completato!")

def crea_bottone_download_per_cartella(nome_cartella):
    if os.path.isdir(nome_cartella) and any(
        os.path.isfile(os.path.join(nome_cartella, f)) for f in os.listdir(nome_cartella)
    ):
        zip_path = f"{nome_cartella}.zip"

        # Elimina ZIP esistente (in caso sia corrotto)
        if os.path.exists(zip_path):
            os.remove(zip_path)

        shutil.make_archive(nome_cartella, 'zip', nome_cartella)

        with open(zip_path, "rb") as f:
            st.download_button(
                label=f"📦 Scarica: {nome_cartella}",
                data=f,
                file_name=f"{nome_cartella}.zip",
                mime="application/zip"
            )

cartelle_output = {
    "baroque_paintings": "📦 Scarica tutto",
    "selected_paintings": "🎯 Scarica solo i filtrati"
}

for cartella, etichetta in cartelle_output.items():
    if os.path.isdir(cartella) and os.listdir(cartella):
        zip_path = f"{cartella}.zip"
        if not os.path.exists(zip_path):
            shutil.make_archive(cartella, 'zip', cartella)

        with open(zip_path, "rb") as f:
            st.download_button(
                label=etichetta,
                data=f,
                file_name=f"{cartella}.zip",
                mime="application/zip"
            )

