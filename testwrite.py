from PIL import Image
import piexif
from datetime import datetime
import os
import pywintypes
import win32file
import win32con
from datetime import datetime

def set_file_time_windows(filepath, fantasy_dt_str):
    fantasy_dt = datetime.strptime(fantasy_dt_str, "%Y:%m:%d %H:%M:%S")
    win_time = pywintypes.Time(fantasy_dt)
    handle = win32file.CreateFile(
        filepath, win32con.GENERIC_WRITE,
        0, None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None
    )
    win32file.SetFileTime(handle, win_time, None, win_time)
    handle.close()



def MetaData(image_path):
    # Load your image

    im = Image.open(image_path)

    # Create EXIF data dictionary
    try:
        exif_dict = piexif.load(im.info['exif'])
    except (KeyError, piexif._exceptions.InvalidImageDataError):
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Set custom metadata
    exif_dict['0th'][piexif.ImageIFD.Artist] = "Cleve Code Erikson".encode()
    exif_dict['0th'][piexif.ImageIFD.ImageDescription] = "Cipher Key says:qporetzuilkhjgfndmsaybxcvw".encode()
    """
    # Date and time
    now = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    """
    fantasy_time_string = "2010:12:22 20:00:00"
    #fantasy_time = "ThirdAge:3021d:09:30 40:00:00"
    fantasy_time = fantasy_time_string.encode()

    exif_dict['0th'][piexif.ImageIFD.DateTime] = fantasy_time
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = fantasy_time
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = fantasy_time
    #Bug fixing
    exif_dict['0th'][piexif.ImageIFD.Make] = b"FantasyCam"
    exif_dict['0th'][piexif.ImageIFD.Model] = b"If Nothing Crys out load, Change the Date to 1.December 2023."
    # GPS data (example: lat=48.8584, lon=2.2945 for Eiffel Tower)
    from fractions import Fraction
    def to_deg(value):
        deg = int(value)
        min_float = (value - deg) * 60
        min = int(min_float)
        sec = int((min_float - min) * 60 * 100)
        return ((deg, 1), (min, 1), (sec, 100))

    def dms_to_rational(degree, minute, second):
        return [
            (int(degree), 1),
            (int(minute), 1),
            (int(second * 100), 100)  # keeping two decimals for seconds
        ]

    # Coordinates: 34°03'17.8"N 118°13'32.2"W
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = 'N'.encode()
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = dms_to_rational(34, 3, 17.8)

    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = 'W'.encode()
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = dms_to_rational(118, 13, 32.2)

    # Convert dict back to bytes
    exif_bytes = piexif.dump(exif_dict)

    # Save image with new EXIF
    output_path = image_path
    im.save(output_path, "jpeg", exif=exif_bytes)

    print("Image saved with updated metadata.")


def append_message_to_image(image_path, message, output_path):
    with open(image_path, "rb") as img_file, open(output_path, "wb") as out_file:
        # Ursprüngliches Bild kopieren
        out_file.write(img_file.read())
        # Nachricht als Text anhängen (UTF-8)
        out_file.write(b"\n---BEGIN HIDDEN MESSAGE---\n")
        out_file.write(message.encode("utf-8"))
        out_file.write(b"\n---END HIDDEN MESSAGE---\n")

# Beispielaufruf

teext="https://github.com/FunPhantasie/Loki ️"
bild1="Contrast.jpg"
bild2="ContrastGhibli.jpg"
MetaData(bild1)
MetaData(bild2)
append_message_to_image(bild1, teext, "Fertig.jpg")
append_message_to_image(bild2, teext, "FertigGhibli.jpg")
fantasy_time_string = "2000:12:22 20:00:00"
set_file_time_windows("Fertig.jpg", fantasy_time_string)
set_file_time_windows("FertigGhibli.jpg", fantasy_time_string)