#4      #muss noch aussortiert werden zB pylintrc
#"test.yaml", "app.py", "check.sh", "pylintrc", "__init__.py", ".gitignore", "misc.xml", "modules.xml", "pythonTestProject.iml", "vcs.xml", "profiles_settings.xml", "test_app.py", "__init__.py"
#6
#"mensa.py", "openligadb.py", "requirements.txt", "rest_api.py", "todo_service.py", ".gitignore", "bundesliga.iml", "misc.xml", "modules.xml", "vcs.xml", "profiles_settings.xml"
#8
#"html_app.py", "requirements.txt", "user_service.py", "__init__.py", "misc.xml", "modules.xml", "python_project.iml", "vcs.xml", "workspace.xml", "profiles_settings.xml", "movies.csv", "hshl.png", "index.html", "movies.html"
#10
#"app.py", "movie_repository.py", "movie_routes.py", "pylintrc", "requirements.txt", "shared.py", "__init__.py", ".gitignore", "misc.xml", "modules.xml", "python_project.iml", "vcs.xml", "profiles_settings.xml", "movies.csv", "layout.html", "movies_by_year.html", "movie_edit.html", "movie_list.html", "pagination.html"
#12
#".gitignore", "06.iml", "misc.xml", "modules.xml", "vcs.xml", "profiles_settings.xml", "app.py", "models.py", "movie_repository.py", "movie_routes.py", "pylintrc", "requirements.txt", "shared.py", "user_repository.py", "user_routes.py", "__init__.py", "misc.xml", "modules.xml", "MovieDatabase.iml", "pythonProject.iml", "vcs.xml", "workspace.xml", "profiles_settings.xml", "movies.csv", "development.yaml", "Dockerfile", "production.yaml", "wordpress.yaml", "layout.html", "login.html", "movie_edit.html", "movie_list.html", "pagination.html"
#Funktioniert auch sehr gut, Nutze v dafür "AlleDateieninEinerListeSamtPfadAusgeben.py"
"""
import os

# List of files to be printed
files = ["C:/Users/Boris Grillborzer/Desktop/04/app.py", "C:/Users/Boris Grillborzer/Desktop/04/test_app.py"]
output_file = "combined.txt"

# Combine files into one
with open(output_file, 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n")

# Print the combined file (change command based on OS)
if os.name == 'nt':  # Windows
    os.system(f'notepad /p {output_file}')
else:  # macOS or Linux
    os.system(f'lpr {output_file}')
"""

import os

def concatenate_files_with_titles(input_directory, output_directory):
    # Sicherstellen, dass das Ausgabe-Verzeichnis existiert
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Extrahiere den Namen des Eingabeordners
    input_directory_name = os.path.basename(os.path.normpath(input_directory))

    # Erstelle den Namen der Ausgabedatei
    output_filename = f"combined{input_directory_name}.txt"

    # Vollständigen Pfad zur Ausgabedatei erstellen
    output_file_path = os.path.join(output_directory, output_filename)

    # Öffne die Ausgabedatei zum Schreiben
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        # Durchlaufe alle Verzeichnisse und Dateien im angegebenen Verzeichnis
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                # Füge den Dateinamen als erste Zeile hinzu
                outfile.write(f"{file}\n")

                # Füge den Inhalt der Datei hinzu
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

                # Füge eine neue Zeile zur Trennung hinzu
                outfile.write("\n")


# Beispiel: Verbinde alle Dateien im aktuellen Verzeichnis und seinen Unterverzeichnissen
# und speichere das Ergebnis im spezifischen Ordner
input_directory = '''C:/Users/Boris Grillborzer/Desktop/06/'''  # Verzeichnis, das durchsucht werden soll
output_directory = '''C:/Users/Boris Grillborzer/Desktop/06/'''  # Pfad zum Ausgabe-Verzeichnis

concatenate_files_with_titles(input_directory, output_directory)