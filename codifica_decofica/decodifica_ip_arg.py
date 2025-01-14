from PIL import Image

def decode_ip_from_pixels(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    ip_bytes = []
    # Estrai i primi 4 pixel per ricostruire l'IP
    for i in range(4):
        r, g, b = pixels[i, 0]  # Supponiamo che l'IP sia codificato nei primi 4 pixel, nel canale R
        ip_bytes.append(str(r))  # Usa solo il canale R

    # Unisci gli ottetti per ottenere l'IP
    return ".".join(ip_bytes)

if __name__ == "__main__":
    # Usa il percorso dell'immagine come input
    import sys
    image_path = sys.argv[1]
    ip = decode_ip_from_pixels(image_path)
    print(ip)  # Stampa l'IP decodificato
