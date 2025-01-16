from PIL import Image

def encode_ip_in_pixels(image_path, output_path, ip_address):
    img = Image.open(image_path)
    pixels = img.load()

    # Splitta l'IP in ottetti e convertili in interi
    ip_bytes = [int(octet) for octet in ip_address.split(".")]

    # Trovo la posizione dell'ultimo pixel (l'angolo in basso a destra dell'immagine)
    width, height = img.size
    last_pixel_x = width - 1
    last_pixel_y = height - 1

    # Modifica i primi 3 pixel per mettere gli ottetti nei canali R, G, B
    pixels[0, 0] = (ip_bytes[0], ip_bytes[1], ip_bytes[2])  # Pixel 1 (R, G, B)
    
    # Modifica l'ultimo pixel per mettere l'ultimo ottetto nel canale R
    pixels[last_pixel_x, last_pixel_y] = (ip_bytes[3], pixels[last_pixel_x, last_pixel_y][1], pixels[last_pixel_x, last_pixel_y][2])  # Pixel ultimo (R, G, B)

    # Salva l'immagine modificata
    img.save(output_path)
    print("Immagine salvata con IP nei pixel.")

encode_ip_in_pixels("Word.png", "Word_with_ip.png", "10.0.2.15")
