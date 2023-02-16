import sys
import PIL
import os
from os import path
from PIL import Image

# Recibe los siguientes argumentos de linea de comandos
# Formato de inputs
# 1 orig_folder   ->  Path del directorio/carpeta con las imágenes, ojo solo puede haber imágenes
# 2 target_dir    ->  Path del directorio/carpeta destino
# 3 format        ->  Formato de la imagen ("jpg","png",(...))


def iterate_folder(orig_folder, target_dir, format):
    for filename in os.listdir(orig_folder):
        process_images(orig_folder, filename, target_dir, format)


# Procesamiento de imágenes
def process_images(orig_folder, filename, target_dir, myformat):
    with Image.open(os.path.join(orig_folder, filename)) as f:
        f_noformat, format = os.path.splitext(filename)
        destiny_joined = os.path.join(target_dir, (f_noformat + myformat))
        f = f.rotate(270)
        f.thumbnail((128, 128))
        if f.mode != 'RGB':
            f = f.convert('RGB')
        f.save(destiny_joined)


# --------- Ejemplo de uso ---------
# iterate_folder("J:/DAM/Codigo/Python/OFolder", J:/DAM/Codigo/Python/folder1", ".png")


iterate_folder(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
