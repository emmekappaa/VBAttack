from PIL import Image

def decode_ip_from_pixels(image_path):
    # Apri l'immagine
    img = Image.open(image_path)
    pixels = img.load()

    # Leggi il primo pixel (dove sono memorizzati i primi 3 ottetti)
    first_pixel = pixels[0, 0]
    ip_bytes = [first_pixel[0], first_pixel[1], first_pixel[2]]  # R, G, B

    # Trovo la posizione dell'ultimo pixel (angolo in basso a destra)
    width, height = img.size
    last_pixel_x = width - 1
    last_pixel_y = height - 1

    # Leggi l'ultimo pixel (dove è memorizzato l'ultimo ottetto nel canale R)
    last_pixel = pixels[last_pixel_x, last_pixel_y]
    ip_bytes.append(last_pixel[0])  # L'ultimo ottetto è nel canale R

    # Unisci i bytes per ottenere l'indirizzo IP
    ip_address = ".".join(map(str, ip_bytes))
    return ip_address

decoded_ip = decode_ip_from_pixels("Word_with_ip.png")
print(f"IP decodificato: {decoded_ip}")
