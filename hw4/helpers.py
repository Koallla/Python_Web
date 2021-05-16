import os
import sys
import shutil
from pathlib import Path
from uuid import uuid4




try:
    from translator import normalize
except ModuleNotFoundError:
    from .translator import normalize



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
def remove_files (name_new_dir, file, path_dir):

    # Путь для новой директории
    path_new_dir = '{}\\{}'.format(path_dir, name_new_dir)

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
def unpack_archive_files(file, path_dir, zip_data):
    zip_data.append(file.name)
    # Создаем путь к директории для распаковки архивов
    path_for_dir_archives = '{}\\{}'.format(path_dir, 'Archives')

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




def create_table_string_format(extention, files_list):
    ''' This funcrion create table for files_list '''

    width = 20
    width_file_list = 60

    string_files = ''
    for file in files_list:
        string_files += '| {:^{width}} | {:^{width}} | {:^{width_file_list}} | \n'.format(' ', ' ', file, width=width, width_file_list=width_file_list)


    title = '| {:^{width}} | {:^{width}} | {:^{width_file_list}} |'.format('Files names', 'Counts', 'Files list',  width=width, width_file_list=width_file_list)
    line = '=' * len(title)
    header = line + '\n' + title + '\n' + line + '\n'

    files_name_and_count = '| {:^{width}} | {:^{width}} | {:_^{width_file_list}} | \n'.format(extention, len(files_list), '', width=width, width_file_list=width_file_list)

    end = '{:=^{width}}'.format('END', width=len(title))

    print(header + files_name_and_count + string_files + end)