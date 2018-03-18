# Создаем папку result
# В папку result  копируем исходники из source
# Открываем папку result
# Запускаем циклом функцию уменьшения размера файлов в папке result на 200 px

import os
import subprocess


# Создаем папку result
# 1 Path to the result
def get_path_for_result(file_name='Result'):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


# 2 Create Result directory in current path
def making_result_directory(path=get_path_for_result()):
    if not os.path.exists(get_path_for_result('Result')):
        return os.mkdir(path)


# Копирование файлов из папки Source
def copy_file_from_directory(name):
    path_source = os.path.join(*[os.path.dirname(os.path.abspath(__file__)), 'Source', name])
    path_destination = get_path_for_result()
    subprocess.run('cp' + ' ' + path_source + ' ' + path_destination, shell=True)


def core():
    image_list = [f for f in os.listdir(get_path_for_result(file_name='Source'))]
    for name in image_list:
        making_result_directory()
        copy_file_from_directory(name)
        subprocess.run(f"sips --resampleWidth 200 {os.path.join(get_path_for_result(),name)}", shell=True)


core()
