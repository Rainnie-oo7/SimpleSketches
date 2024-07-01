import os
import random
import shutil


def move_files(src_dir, dest_dir1, dest_dir2):
    # Erstelle die Zielverzeichnisse, falls sie nicht existieren
    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)

    # Liste aller Dateien im Quellverzeichnis
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    # Anzahl der Dateien
    total_files = len(files)

    # Berechne die Anzahl der Dateien für jeden Ordner
    num_files_dest1 = int(total_files * 1 / 3)
    num_files_dest2 = total_files - num_files_dest1

    # Mische die Dateien zufällig
    random.shuffle(files)

    # Verschiebe 2/5 der Dateien in dest_dir1 und 3/5 in dest_dir2
    for i, file in enumerate(files):
        src_path = os.path.join(src_dir, file)
        if i < num_files_dest1:
            dest_path = os.path.join(dest_dir1, file)
        else:
            dest_path = os.path.join(dest_dir2, file)
        shutil.move(src_path, dest_path)


# Beispielnutzung
source_directory = '''C:/Users/Boris Grillborzer/Desktop/eisenerzIV'''
destination_directory1 = '''C:/Users/Boris Grillborzer/Desktop/train_data/images/val'''
destination_directory2 = '''C:/Users/Boris Grillborzer/Desktop/train_data/images/train'''

move_files(source_directory, destination_directory1, destination_directory2)
