

def append_message_to_image(image_path, message, output_path):
    with open(image_path, "rb") as img_file, open(output_path, "wb") as out_file:
        # Ursprüngliches Bild kopieren
        out_file.write(img_file.read())
        # Nachricht als Text anhängen (UTF-8)
        out_file.write(b"\n---BEGIN HIDDEN MESSAGE---\n")
        out_file.write(message.encode("utf-8"))
        out_file.write(b"\n---END HIDDEN MESSAGE---\n")

# Beispielaufruf
append_message_to_image("duck.jpg", "Dies ist Tims geheime Botschaft ️", ""
                                                                             "hi.jpg")
