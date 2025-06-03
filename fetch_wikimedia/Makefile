VENV := .venv-wikimedia
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

run: $(VENV)/bin/activate
	@echo "🔧 Installo librerie di sistema se mancano..."
	sudo apt-get update -qq && sudo apt-get install -y -qq libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 > /dev/null
	$(PIP) install -r requirements.txt
	$(PY) main.py

$(VENV)/bin/activate:
	@python3 -m venv $(VENV)
	@echo "[🐍] Ambiente virtuale creato in $(VENV)"

clean:
	rm -rf $(VENV)
	find . -type d -name '__pycache__' -exec rm -r {} +
