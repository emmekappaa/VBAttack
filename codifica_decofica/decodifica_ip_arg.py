from PIL import Image

def decode_ip_from_pixels(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    binary_message = ''
    binary_index = 0
    
    # Leggi solo i primi 32 bit (equivalenti a 4 ottetti di un indirizzo IP)
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            
            # Estrai i bit dai canali R, G, B
            if binary_index < 32:  # Solo i primi 32 bit sono necessari per l'IP
                binary_message += str(r & 1)  # Estrai l'LSB di R
                binary_index += 1
            if binary_index < 32:
                binary_message += str(g & 1)  # Estrai l'LSB di G
                binary_index += 1
            if binary_index < 32:
                binary_message += str(b & 1)  # Estrai l'LSB di B
                binary_index += 1
            
            # Fermati se hai letto 32 bit
            if binary_index >= 32:
                break
        if binary_index >= 32:
            break
    
    # Ora converti i 32 bit in un indirizzo IP
    ip_octets = [int(binary_message[i:i+8], 2) for i in range(0, 32, 8)]
    ip_address = '.'.join(map(str, ip_octets))
    
    return ip_address

if __name__ == "__main__":
    import sys    
    image_path = sys.argv[1]
    decoded_ip = decode_ip_from_pixels(image_path)
    print(decoded_ip)
