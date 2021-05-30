from aiopath import AsyncPath
import asyncio
import os
import sys
import shutil
from pathlib import Path
from uuid import uuid4

from prettytable import PrettyTable


try:
    from translator import normalize
except ModuleNotFoundError:
    from .translator import normalize

# TODO
# Пофиксить NoneType 


def get_path():
    path_dir = None
    try:
        path_dir = sys.argv[1]
    except IndexError:
        path_dir = input('Enter path to directory: ')
    if Path(path_dir).exists():
        path_dir = Path(path_dir)
        return path_dir
    else:
        print('You entered wrong path! Please, try again!')
        get_path()
root_path_dir = get_path()


# Списки для имен файлов
files_dict = {
'Images': [],
'Video': [],
'Documents': [],
'Music': [],
'Zip_data': [],
'Unknown_files': []}




# Фильтры для файлов
photo_filter = ("jpeg", "png", "jpg", "svg")
video_filter = ("avi", "mp4", "mov", "mkv")
docs_filter = ("doc", "docx", "txt", "pdf", "xlsx", "pptx")
music_filter = ("mp3", "ogg", "wav", "amr")
soft_filter = ("exe", "mdf", "mds")
zip_data_filter = ("zip", "bztar", "gztar", "tar", "xztar")
ignore_dir = ('Images', 'Video', 'Audio', 'Documents', 'Archives', 'Unknown_files')


# Выделение уникальных расширений
def extensions(file, container):
    container.add(file.suffix[1:].lower())

# Сообщение: Файл существует!
def message_file_exists(file_name):
    print(f'Файл {file_name} уже существует')


# Перевод имени файлов и их переименование (для цикла path.iterdir())
async def rename_files(file):
    ext = file.suffix
    file_name_without_ext = file.name.removesuffix(ext)
    file_name_translated = await normalize(file_name_without_ext)
    file_name_with_ext = '{}{}'.format(file_name_translated, ext)
    p = AsyncPath(file)
    parent_dir = p.parent
    full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
    try:
        await p.rename(full_path_new_file)
    except FileExistsError: 
        message_file_exists(file.name)
        file_name_with_ext = '{}_id_{}{}'.format(file_name_translated, uuid4(), ext)
        full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
        await p.rename(full_path_new_file)



# async def rename_files(file):
#     ext = file.suffix
#     file_name_without_ext = file.name.removesuffix(ext)
#     file_name_with_ext = '{}_id_{}{}'.format('абвгдеёж', uuid4(), ext)
#     p = AsyncPath(file)
#     parent_dir = p.parent
#     full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
#     try:
#         await p.rename(full_path_new_file)
#     except FileExistsError: 
#         message_file_exists(file.name)
#         file_name_with_ext = '{}_id_{}{}'.format(file_name_translated, uuid4(), ext)
#         full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
#         await p.rename(full_path_new_file)



# Создание папки и перемещение в нее файлов определенного типа
def remove_files(name_new_dir, file):

    # Путь для новой директории
    path_new_dir = '{}\\{}'.format(root_path_dir, name_new_dir)

    # Создаем новую директорию и перемещаем в нее файл
    if os.path.exists(path_new_dir):
        try:
            shutil.move(file, path_new_dir)
        except:
            file_name = f"{file.stem}_id_{uuid4()}{file.suffix}"
            parent_dir = file.parent
            full_path_to_file = f'{parent_dir}\{file_name}'
            new_path_rename_file = file.rename(full_path_to_file)
            files_dict[name_new_dir].append(file_name)
            shutil.move(new_path_rename_file, path_new_dir)
    else:
        os.mkdir(path_new_dir)
        shutil.move(file, path_new_dir)


# Создание папки, подпаки и распаковка архива 
def unpack_archive_files(file):

    # Создаем путь к директории для распаковки архивов
    path_for_dir_archives = '{}\\{}'.format(root_path_dir, 'Archives')

    # Создаем путь к поддиректории для распаковки одного архива
    path_for_dir_unpack = '{}\\{}'.format(path_for_dir_archives, file.name.removesuffix(file.suffix[:]))

    if os.path.exists(path_for_dir_archives):
        try:
            # Распаковываем архив в подпапку и удаляем оригинал 
            os.mkdir(path_for_dir_unpack)
            shutil.unpack_archive(file, path_for_dir_unpack)
            os.remove(file)

        except (FileExistsError, shutil.Error):
            # shutil.unpack_archive(file, path_for_dir_unpack)
            message_file_exists(file.name)
    else:
        os.mkdir(path_for_dir_archives)
        os.mkdir(path_for_dir_unpack)
        # Распаковываем архив
        shutil.unpack_archive(file, path_for_dir_unpack)
        os.remove(file)


# Сортировка файлов по спискам и вызов функции перемещения файлов
def moving_files(file):
    ext_lower = file.suffix[1:].lower()

    if ext_lower in (photo_filter):
        files_dict['Images'].append(file.name)
        remove_files('Images', file)
        
    elif ext_lower in (video_filter):
        files_dict['Video'].append(file.name)
        remove_files('Video', file)

    elif ext_lower in (docs_filter):
        files_dict['Documents'].append(file.name)
        remove_files('Documents', file)

    elif ext_lower in (music_filter):
        files_dict['Music'].append(file.name)
        remove_files('Music', file)
    
    elif ext_lower in (zip_data_filter):
            files_dict['Zip_data'].append(file.name)
            unpack_archive_files(file)
        
    else:
        files_dict['Unknown_files'].append(file.name)
        remove_files('Unknown_files', file)


def create_table(extention, files_list):
    ''' This funcrion create table for files_list '''
    x = PrettyTable()
    title = ["ID", "File type", "File name",  "File extention"]
    x.field_names = title
    if files_list:
        rows = []
        for idx, file in enumerate(files_list):
            file = Path(file)
            rows.append([idx + 1, extention, file.stem, file.suffix[1:].lower()])

        x.add_rows(rows)
        print(x)
    else:
        x.add_row([0, '-', '-', '-'])
        print(x)



def show_result():
    create_table('Images', files_dict['Images'])
    create_table('Video', files_dict['Video'])
    create_table('Documents', files_dict['Documents'])
    create_table('Music', files_dict['Music'])
    create_table('Zip_data', files_dict['Zip_data'])
    create_table('Unknown_files', files_dict['Unknown_files']) 


