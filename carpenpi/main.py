#Creating directory for R files if it does not exist
# Download files using download files.py
#Downloading Data Carpentry website using httrack

import wget
from pathlib import Path, PurePath
from carpenpi import urls
from carpenpi import downloadfiles
from carpenpi import download_lessons

def create_carpenpi_dir(directory=Path.home()):
    folder_path = Path(directory, Path('carpenpi'))
    if not folder_path.is_dir():
        print("\nCreating carpenpi folder in " + str(directory))
        Path.mkdir(folder_path, parents=True)
    return str(folder_path)

def download(carpenpi_dir):
    for url in urls.urls:
        downloadfiles.download_files(url, carpenpi_dir=carpenpi_dir)
    download_lessons.download_lessons(carpenpi_dir)
