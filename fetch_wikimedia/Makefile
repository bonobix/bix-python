VENV = .venv_wikimedia

run: $(VENV)/bin/activate
	. $(VENV)/bin/activate && \
	pip install -r requirements.txt && \
	python main.py

$(VENV)/bin/activate:
	@python3 -m venv $(VENV)
	@echo "[🐍] Ambiente virtuale creato in $(VENV)"

clean:
	rm -rf $(VENV)
	find . -type d -name '__pycache__' -exec rm -r {} +
