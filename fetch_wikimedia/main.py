import os
import subprocess

# Lista degli script da eseguire in ordine
SCRIPTS = [
    "fetch_images.py",
    "entropy_filter.py",
    "laplacian_filter.py"
]

def run_script(script):
    print(f"\n🔄 Eseguo: {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"[💥] Errore in {script}:\n{result.stderr}")

def main():
    print("🎨 Inizio pipeline arte barocca...\n")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    for script in SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"[⚠️] Script non trovato: {script}")

    print("\n🏁 Pipeline completata! Guarda in 'selected_paintings' per i risultati finali.")

if __name__ == "__main__":
    main()
