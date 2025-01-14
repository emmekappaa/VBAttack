# server.py
import os
from flask import Flask, request

app = Flask(__name__)

# Directory dove verranno salvati i file ricevuti
save_directory = os.path.expanduser("~/Desktop/C2")

# Crea la cartella C2 se non esiste
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(save_directory, file.filename))  # Salva il file nella directory C2
    return "File ricevuto con successo!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Esegui il server sulla porta 5000
