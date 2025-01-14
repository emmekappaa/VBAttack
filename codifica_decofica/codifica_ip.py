from PIL import Image

def encode_ip_in_pixels(image_path, output_path, ip_address):

    img = Image.open(image_path)
    pixels = img.load()

    # itero otteti di stringhe e trasformo in int
    ip_bytes = [int(octet) for octet in ip_address.split(".")]

    # Modifica i primi pixel con i valori dell'IP
    for i in range(4):
        pixels[i, 0] = (ip_bytes[i], 0, 0)  # Cambia il canale R

    # Salva l'immagine modificata
    img.save(output_path)
    print("Immagine salvata con IP nei pixel.")

encode_ip_in_pixels("Word.png", "Word_with_ip.png", "192.168.1.100")
