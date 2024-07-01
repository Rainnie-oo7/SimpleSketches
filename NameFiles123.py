import os
def rename_files(directory):
    # Liste aller Dateien im Verzeichnis
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sortiere die Dateien für konsistente Ergebnisse
    files.sort()

    # Benenne jede Datei aufsteigend um
    for i, file in enumerate(files):
        # Extrahiere die Dateierweiterung
        file_extension = os.path.splitext(file)[1]

        # Neuer Dateiname mit aufsteigender Nummer
        new_name = f"{i + 1}{file_extension}"

        # Vollständige Pfade
        src_path = os.path.join(directory, file)
        dest_path = os.path.join(directory, new_name)

        # Datei umbenennen
        os.rename(src_path, dest_path)


# Beispielnutzung
directory_path = '''C:/Users/Boris Grillborzer/Desktop/train_data/images/train'''
directory_pathval = '''C:/Users/Boris Grillborzer/Desktop/train_data/images/val'''
rename_files(directory_path)
rename_files(directory_pathval)