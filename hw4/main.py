import concurrent.futures
from pathlib import Path
import os
import sys
import shutil
from time import sleep
from uuid import uuid4




try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import *


path = root_path_dir

# Получение всех файлов, в том числе вложенных, 
def get_files_list(path):
        # try:
        #     pass
        # except FileNotFoundError:
        #     print('You entered wrong path! Please, try again!')
        #     return



    for file in path.iterdir():
        rename_files(file) # Переименовываем файлы


    for file in path.iterdir():
        if file.is_file():
            # Перемещение файлов
            moving_files(file)
                
        elif file.is_dir() and file.name in ignore_dir:
            continue
        else:
            # Создаем новый путь
            path_for_recursion = Path(f'{file.parent}\{file.name}')

            # Рекурсия
            get_files_list(path_for_recursion)

            # Удаление пустых директорий
            try:
                Path.rmdir(file)
            except OSError:
                continue


get_files_list(path)

show_result()
