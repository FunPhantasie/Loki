def extract_message_from_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        try:
            start = data.index(b"---BEGIN HIDDEN MESSAGE---") + len(b"---BEGIN HIDDEN MESSAGE---")
            end = data.index(b"---END HIDDEN MESSAGE---")
            message = data[start:end].decode("utf-8", errors="ignore").strip()
            print("Gefundene Nachricht:\n", message)
        except ValueError:
            print("Keine versteckte Nachricht gefunden.")

# Beispielaufruf
extract_message_from_image("hi.jpg")
