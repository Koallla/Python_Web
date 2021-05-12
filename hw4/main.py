import os
import sys
import shutil
from pathlib import Path
from uuid import uuid4


# Какая-то проблемма с импортом модуля, поэтому завернул в try/except
try:
    from translator import normalize
except ModuleNotFoundError:
    from .translator import normalize


try:
    path_dir = sys.argv[1]
except IndexError:
    path_dir = input('Enter path to directory: ')


path = Path(path_dir)

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
ignore_dir = ('images', 'video', 'audio', 'documents', 'archives', 'unknown_files')


# Сообщение: Файл существует!
def message_file_exists(file_name):
    print(f'Файл {file_name} уже существует')
    

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
        file_name_with_ext = '{}_id{}{}'.format(file_name_translated, uuid4(), ext)
        full_path_new_file = '{}\{}'.format(parent_dir, file_name_with_ext)
        p.rename(full_path_new_file)
        


# Создание папки и перемещение в нее файлов определенного типа
def remove_files (name_new_dir, file):

    # Путь для новой директории
    path_new_dir = '{}\\{}'.format(path_dir, name_new_dir)
    p = Path(path_new_dir)

    # Создаем новую директорию и перемещаем в нее файл

    if os.path.exists(path_new_dir):
        shutil.move(file, path_new_dir)
    else:
        os.mkdir(path_new_dir)
        shutil.move(file, path_new_dir)



# Создание папки, подпаки и распаковка архива 
def unpack_archive_files(file):
    zip_data.append(file.name)
    # Создаем путь к директории для распаковки архивов
    path_for_dir_archives = '{}\\{}'.format(path_dir, 'archives')

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


# Получение всех файлов, в том числе вложенных, 
def get_files_list(path=Path(path_dir)):

    
    # Перевод всех файлов на латиницу
    for file in path.iterdir():
        rename_files(file)

    for file in path.iterdir():
        if file.is_file():

            ext_lower = file.suffix[1:].lower()

            if ext_lower in (photo_filter):
                photo.append(file.name)
                remove_files('images', file)
                
            elif ext_lower in (video_filter):
                video.append(file.name)
                remove_files('video', file)

            elif ext_lower in (docs_filter):
                docs.append(file.name)
                remove_files('documents', file)

            elif ext_lower in (music_filter):
                music.append(file.name)
                remove_files('audio', file)
            
            
            # elif ext_lower in (zip_data_filter):
            #     unpack_archive_files(file)
            

            # Как я понял из условия задания, неизвестные файлы мы не трогаем... 
            # else:
            #     unknown_files.append(file.name)
            #     remove_files('unknown_files', file)

                
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


if photo or video or docs or music or zip_data:
    create_table_string_format('photo', photo)
    create_table_string_format('video', video)
    create_table_string_format('docs', docs)
    create_table_string_format('music', music)
    create_table_string_format('zip_data', zip_data)