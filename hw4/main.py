from aiopath import AsyncPath
import asyncio
# from pathlib import Path
import os
import sys
import shutil
from time import sleep, time
from uuid import uuid4




try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import *

path = root_path_dir


# # Получение всех файлов, в том числе вложенных, 
# def get_files_list(path):
#     start_time = time()

#     for file in path.iterdir():
#         rename_files(file) # Переименование файлов
#     print('Finish:', time() - start_time)

#     # for file in path.iterdir():
#     #     if file.is_file():
#     #         moving_files(file) # Перемещение файлов
                
#     #     elif file.is_dir() and file.name in ignore_dir:
#     #         continue
#     #     else:
#     #         # Создаем новый путь
#     #         path_for_recursion = Path(f'{file.parent}\{file.name}')

#     #         # Рекурсия
#     #         get_files_list(path_for_recursion)

#     #         # Удаление пустых директорий
#     #         try:
#     #             Path.rmdir(file)
#     #         except OSError:
#     #             continue


# get_files_list(path)

# show_result()

# sync rename Finish: 0.8864912986755371


# ==================================================================
# async
async def main(path):
    start_time = time()

    futures = [rename_files(file) for file in path.iterdir()]
    await asyncio.gather(*futures)

    print(time() - start_time)

asyncio.run(main(path))