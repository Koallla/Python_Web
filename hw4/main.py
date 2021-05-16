import concurrent.futures
from pathlib import Path
import os
import sys
import shutil
from uuid import uuid4


try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import *


# try:
#     path_dir = sys.argv[1]
# except IndexError:
#     path_dir = input('Enter path to directory: ')

path_dir = 'D:\Test'
path = Path(path_dir)

photo = []
video = []
docs = []
music = []
zip_data = []
unknown_files = []



# Получение всех файлов, в том числе вложенных, 
def get_files_list(path=Path(path_dir)):

    
    # Перевод всех файлов на латиницу
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(rename_files, [file for file in path.iterdir() if file.is_file()])

    # for file in path.iterdir():
    #     rename_files(file)



# Вынести всю логику в функцию remove_files()
    for file in path.iterdir():
        if file.is_file():

            ext_lower = file.suffix[1:].lower()

            if ext_lower in (photo_filter):
                photo.append(file.name)
                remove_files('Images', file, path_dir)
                
            elif ext_lower in (video_filter):
                video.append(file.name)
                remove_files('Video', file, path_dir)

            elif ext_lower in (docs_filter):
                docs.append(file.name)
                remove_files('Documents', file, path_dir)

            elif ext_lower in (music_filter):
                music.append(file.name)
                remove_files('Audio', file, path_dir)
            
            
            elif ext_lower in (zip_data_filter):
                zip_data.append(file.name)
                unpack_archive_files(file, path_dir, zip_data)
            

            else:
                unknown_files.append(file.name)
                remove_files('Unknown_files', file, path_dir)

                
    #     elif file.is_dir() and file.name in ignore_dir:
    #         continue

    #     else:
    #         # Создаем новый путь
    #         path_for_recursion = Path(f'{file.parent}\{file.name}')

    #         # Рекурсия
    #         get_files_list(path_for_recursion)

    #         # Удаление пустых директорий
    #         try:
    #             Path.rmdir(file)
    #         except OSError:
    #             continue

get_files_list(path)









# if photo or video or docs or music or zip_data:
#     create_table_string_format('photo', photo)
#     create_table_string_format('video', video)
#     create_table_string_format('docs', docs)
#     create_table_string_format('music', music)
#     create_table_string_format('zip_data', zip_data)