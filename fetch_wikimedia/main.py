import subprocess
import sys
import os

SCRIPTS = ["fetch-dipinti.py", "filtra-entropia.py", "filtro-laplaciano.py"]

def run_script(script):
    print(f"\n Eseguo: {script}")
    try:
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errore in {script}:\n{result.stderr}")
    except Exception as e:
        print(f"Eccezione eseguendo {script}: {e}")

def main():
    for script in SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"[❓] Script mancante: {script}")

if __name__ == "__main__":
    main()
