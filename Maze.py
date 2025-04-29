import os
import random
import string

# Basisordner
root = "RaetselOrdner"

# Strukturdefinition
erste_ebene = [ "2021", "2000"]
monate = ["Januar", "Februar", "März", "April", "Mai"]
tage = ["01", "02", "03", "04", "05"]
uhrzeit=["5","1"]
namen_ebene="Häuser"
# Funktion zur String-Erzeugung
def zufallsstring(length=17):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Struktur aufbauen und Textdateien einfügen
for ordner in erste_ebene:
    for monat in monate:
        for tag in tage:
            for uhr in uhrzeit:
                pfad = os.path.join(root, ordner, monat, tag,uhr)
                os.makedirs(pfad, exist_ok=True)

                dateipfad = os.path.join(pfad, "hinweis.txt")
                with open(dateipfad, "w") as f:
                    f.write(zufallsstring())

# 🔡 Echte, nicht wiederholte Wörter
ebene1_worte = [
    "apfel", "buechse", "garten", "lampe", "tafel",
    "fenster", "kissen", "leiter", "sofa", "uhr",
    "kiste", "stuhl", "bett", "schrank", "tisch",
    "vase", "topf", "lappen", "glas", "seife",
    "wand", "boden", "dach", "decke", "fliese"
]
ebene2_worte = [
    "schluessel", "kerze", "messer", "buch", "gabel",
    "löffel", "dose", "schale", "regal", "korb",
    "rahmen", "tuch", "vorhang", "poster", "teppich",
    "radio", "kamera", "akku", "fahne", "socke",
    "keramik", "pflanze", "schraube", "wecker", "dose"
]
ebene3_worte = ["spiegel", "tuer"]  # nur 2, alternierend

# Shuffle, um willkürlich zu kombinieren
random.shuffle(ebene1_worte)
random.shuffle(ebene2_worte)

# 25 einzigartige Paare bilden und mit 2 Endwörtern kombinieren
for i in range(25):
    ordner1 = ebene1_worte[i]
    ordner2 = ebene2_worte[i]
    ordner3 = ebene3_worte[i % 2]  # abwechselnd "spiegel" und "tuer"

    pfad = os.path.join(root, "Häuser", ordner1, ordner2, ordner3)
    os.makedirs(pfad, exist_ok=True)
    with open(os.path.join(pfad, "hinweis.txt"), "w") as f:
        f.write(zufallsstring())

# Hinweis im Hauptordner "Häuser"
with open(os.path.join(root, "Häuser", "README.txt"), "w") as f:
    f.write("Behalte diesen Ordner im Hinterkopf – später wichtig!")