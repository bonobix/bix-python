import streamlit as st
import os
import shutil
import json

from fetch_wikimedia.scripts.fetch_dipinti import main as fetch_images
from fetch_wikimedia.scripts.filtro_entropia import main as entropy_filter
from fetch_wikimedia.scripts.filtro_laplaciano import main as laplace_filter

st.set_page_config(page_title="Wikimedia Art Filter", layout="centered")

st.title("🎨 Wikimedia Art Filter")
st.write("Scarica dipinti, filtra per qualità, e seleziona le immagini migliori.")

if st.button("🔍 Scarica immagini"):
    st.write("Inizio download...")
    fetch_images()
    st.success("Download completato!")

if st.button("🧠 Filtro entropia"):
    st.write("Filtraggio entropico in corso...")
    entropy_filter()
    st.success("Filtro entropia completato!")

if st.button("🌀 Filtro Laplaciano"):
    st.write("Analisi del dettaglio in corso...")
    laplace_filter()
    st.success("Filtro Laplaciano completato!")

if st.button("📂 Apri cartella finale"):
    st.write("Apri la cartella `selected_paintings` sul tuo sistema.")

user_category = st.text_input("🎯 Categoria Wikimedia:", "Paintings by Jan van Goyen")

if st.button("🔄 Aggiorna categoria"):
    config_path = os.path.join("fetch_wikimedia", "scripts", "config.json")
    try:
        with open(config_path, "w") as f:
            json.dump({"CATEGORY_NAME": user_category}, f)
        st.success(f"✅ Categoria aggiornata a: {user_category}")
    except Exception as e:
        st.error(f"❌ Errore durante l'aggiornamento: {e}")

def crea_bottone_download_per_cartella(nome_cartella):
    if os.path.isdir(nome_cartella) and os.listdir(nome_cartella):
        zip_path = f"{nome_cartella}.zip"
        if not os.path.exists(zip_path):
            shutil.make_archive(nome_cartella, 'zip', nome_cartella)

        with open(zip_path, "rb") as f:
            st.download_button(
                label=f"📦 Scarica: {nome_cartella}",
                data=f,
                file_name=f"{nome_cartella}.zip",
                mime="application/zip"
            )

cartelle_output = ["selected_paintings", "baroque_paintings"]
for cartella in cartelle_output:
    crea_bottone_download_per_cartella(cartella)
