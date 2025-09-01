# 🖼️ Fetch Paintings on Wikimedia (and more!)

Questo modulo scarica dipinti da Wikimedia Commons, poi filtra le immagini in base a:

- **Entropia** (per evitare immagini piatte o troppo compresse)
- **Varianza del Laplaciano** (per valutare la nitidezza)

## 📦 Struttura degli script

- `fetch-dipinti.py` – Scarica immagini da Wikimedia usando API
- `verifica-entropia.py` – Rimuove immagini con entropia troppo bassa
- `filtro-laplaciano.py` – Filtra e copia le immagini nitide in `selected_paintings/`

## 🚀 Come si usa

```bash
# 1. Scarica le immagini
python fetch_images.py

# 2. Rimuovi quelle a bassa entropia
python entropy_filter.py

# 3. Seleziona le più nitide
python laplacian_filter.py
