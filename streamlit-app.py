import streamlit as st
import os

from fetch_wikimedia.scripts.fetch_dipinti import main as fetch_images
from fetch_wikimedia.scripts.filtro_entropia import main as entropy_filter
from fetch_wikimedia.scripts.filtro_laplaciano import main as laplace_filter

st.set_page_config(page_title="🎨 Wikimedia Art Filter", layout="centered")
st.title("🎨 Wikimedia Art Filter")
st.write("Scarica dipinti, filtra per qualità, e seleziona le immagini migliori.")

# 🧙‍♂️ Scegli la categoria Wikimedia
user_category = st.text_input("📚 Inserisci il nome della categoria Wikimedia (es. Baroque paintings):", "Paintings by Jan van Goyen")

if st.button("🔄 Aggiorna categoria"):
    path = os.path.join("fetch_wikimedia", "scripts", "fetch_dipinti.py")
    if os.path.exists(path):
        with open(path, "r") as f:
            lines = f.readlines()
        with open(path, "w") as f:
            for line in lines:
                if line.strip().startswith("CATEGORY_NAME"):
                    f.write(f'CATEGORY_NAME = "{user_category}"\n')
                else:
                    f.write(line)
        st.success(f"✅ Categoria aggiornata a: {user_category}")
    else:
        st.error("❌ File fetch_dipinti.py non trovato!")
