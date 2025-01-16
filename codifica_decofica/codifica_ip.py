from PIL import Image

def encode_ip_in_pixels(image_path, output_path, ip_address):
    # Converti gli ottetti dell'IP in binario
    ip_octets = [int(octet) for octet in ip_address.split('.')] #lista di valori interi
    binary_message = ''.join(format(octet, '08b') for octet in ip_octets) #converto in binario e passo a stringhe
    
    # Carica l'immagine
    img = Image.open(image_path)
    pixels = img.load()
    
    # Verifica che l'immagine abbia abbastanza pixel per contenere il messaggio
    width, height = img.size
    total_pixels = width * height
    if len(binary_message) > total_pixels * 3:  # Ogni pixel ha 3 canali (R, G, B)
        raise ValueError("L'immagine non ha abbastanza spazio per il messaggio.")
    
    # Codifica il messaggio nei bit meno significativi
    binary_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Sostituisci i bit meno significativi con il messaggio

            # (r & 0xFE) AND BIT A BIT CON 11111110

            if binary_index < len(binary_message):
                r = (r & 0xFE) | int(binary_message[binary_index])  # Cambia LSB del canale R
                binary_index += 1
            if binary_index < len(binary_message):
                g = (g & 0xFE) | int(binary_message[binary_index])  # Cambia LSB del canale G
                binary_index += 1
            if binary_index < len(binary_message):
                b = (b & 0xFE) | int(binary_message[binary_index])  # Cambia LSB del canale B
                binary_index += 1
            
            pixels[x, y] = (r, g, b)
    
    # Salva l'immagine modificata
    img.save(output_path)

encode_ip_in_pixels("Word.png", "Word_with_ip.png", "10.0.2.15")
