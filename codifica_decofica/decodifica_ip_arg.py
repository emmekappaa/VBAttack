from PIL import Image

def decode_ip_from_pixels(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    ip_bytes = []
    
    # Estrai il primo pixel (contenente R, G, B per i primi 3 ottetti)
    first_pixel = pixels[0, 0]
    ip_bytes.append(str(first_pixel[0]))  # Ottetto 1 (R)
    ip_bytes.append(str(first_pixel[1]))  # Ottetto 2 (G)
    ip_bytes.append(str(first_pixel[2]))  # Ottetto 3 (B)
    
    # Estrai l'ultimo pixel (contenente l'ultimo ottetto nel canale R)
    width, height = img.size
    last_pixel = pixels[width - 1, height - 1]
    ip_bytes.append(str(last_pixel[0]))  # Ottetto 4 (R dell'ultimo pixel)
    
    # Unisci gli ottetti per ottenere l'IP
    return ".".join(ip_bytes)

if __name__ == "__main__":
    # Usa il percorso dell'immagine come input
    import sys
    image_path = sys.argv[1]
    ip = decode_ip_from_pixels(image_path)
    print(ip)

