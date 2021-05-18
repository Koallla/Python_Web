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


def get_path():
    path_dir = None
    try:
        path_dir = sys.argv[1]
    except IndexError:
        path_dir = input('Enter path to directory: ')

    path_dir = Path(path_dir)
    return path_dir

root_path_dir = get_path()


# Списки для имен файлов
photo = []
video = []
docs = []
music = []
zip_data = []
unknown_files = []



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


# Перевод имени файлов и их переименование (для цикла path.iterdir())
def rename_files (file):
    ext = file.suffix
    file_name_without_ext = file.name.removesuffix(ext)
    file_name_translated = normalize(file_name_without_ext)
    file_name_with_ext = '{}{}'.format(file_name_translated, ext)
    p = Path(file)
    parent_dir = p.parent
    full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
    try:
        p.rename(full_path_new_file)
    except FileExistsError: 
        message_file_exists(file.name)
        file_name_with_ext = '{}_id_{}{}'.format(file_name_translated, uuid4(), ext)
        full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
        p.rename(full_path_new_file)


# Сообщение: Файл существует!
def message_file_exists(file_name):
    print(f'Файл {file_name} уже существует')


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
            full_path_to_file = f'{file_name}'
            new_path_rename_file = file.rename(full_path_to_file)
            shutil.move(new_path_rename_file, path_new_dir)
    else:
        os.mkdir(path_new_dir)
        shutil.move(file, path_new_dir)


# Создание папки, подпаки и распаковка архива 
def unpack_archive_files(file, zip_data):

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
        photo.append(file.name)
        remove_files('Images', file)
        
    elif ext_lower in (video_filter):
        video.append(file.name)
        remove_files('Video', file)

    elif ext_lower in (docs_filter):
        docs.append(file.name)
        remove_files('Documents', file)

    elif ext_lower in (music_filter):
        music.append(file.name)
        remove_files('Audio', file)
    
    elif ext_lower in (zip_data_filter):
            zip_data.append(file.name)
            unpack_archive_files(file, zip_data)
        
    else:
        unknown_files.append(file.name)
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
    create_table('Photo', photo)
    create_table('Video', video)
    create_table('Docs', docs)
    create_table('Music', music)
    create_table('Zip_data', zip_data)
    create_table('Unknow_files', unknown_files)