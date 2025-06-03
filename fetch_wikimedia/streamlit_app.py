import streamlit as st
import os
from fetch-dipinti import main as fetch_images
from filtro-entropia import main as entropy_filter
from filtro-laplaciano import main as laplace_filter

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
