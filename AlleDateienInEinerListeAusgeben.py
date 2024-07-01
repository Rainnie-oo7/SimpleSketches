import os

def list_files_in_one_line(directory):
    # Eine Liste zum Speichern aller Dateinamen
    all_files = []

    # Durchlaufe alle Verzeichnisse und Dateien im angegebenen Verzeichnis
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Füge nur den Dateinamen zur Liste hinzu
            all_files.append(f'"{file}"')

    # Gebe alle Dateinamen in einer Zeile aus, getrennt durch ein Komma
    print(", ".join(all_files))

# Beispiel: Gebe alle Dateien im aktuellen Verzeichnis und seinen Unterverzeichnissen aus
list_files_in_one_line('C:/Users/Boris Grillborzer/Desktop/04')

