from PIL import Image

def crop_image(image_path, target_size, save=True, output_path=""):
    # Öffne das Bild mit Pillow
    image = Image.open(image_path)

    # Bestimme die aktuellen Abmessungen des Bildes
    width, height = image.size

    # Bestimme die Zielabmessungen
    target_width, target_height = target_size

    # Berechne das Verhältnis der Zielgröße zu den aktuellen Abmessungen
    resize_ratio = target_height / height

    # Berechne die neuen Abmessungen
    new_width = int(width * resize_ratio)
    new_height = int(height * resize_ratio)

    # Skaliere das Bild auf die neuen Abmessungen
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Bestimme den Startpunkt für das Zuschneiden
    left = (new_width - target_width) / 2
    top = (new_height - target_height) / 2
    right = (new_width + target_width) / 2
    bottom = (new_height + target_height) / 2

    # Schneide das Bild auf die Zielgröße zu
    cropped_image = resized_image.crop((left, top, right, bottom))

    if save:
        # Speichere das zugeschnittene Bild
        cropped_image.save(output_path)

    #print("Das Bild wurde erfolgreich zugeschnitten und unter", output_path, "gespeichert.")

    return cropped_image

# Beispielaufruf
#image_path = "data/watches/watches_marc/images/MG01338.jpg"  # Pfad zum Eingangsbild
#output_path = "output.jpg"  # Pfad zum gespeicherten zugeschnittenen Bild
#target_size = (406, 512)  # Zielgröße des zugeschnittenen Bildes (Breite, Höhe)

#crop_image(image_path, output_path, target_size)
