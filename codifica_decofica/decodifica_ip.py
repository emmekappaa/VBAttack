from PIL import Image

def decode_ip_from_pixels(image_path):
    # Apri l'immagine
    img = Image.open(image_path)
    pixels = img.load()

    # Leggi i valori dei primi 4 pixel
    ip_bytes = [pixels[i, 0][0] for i in range(4)]
    ip_address = ".".join(map(str, ip_bytes))
    return ip_address

decoded_ip = decode_ip_from_pixels("Word_with_ip.png")
print(f"IP decodificato: {decoded_ip}")
