'''
Створіть функціонал для розпакування архіву.

Зробіть import пакету shutil

Створіть функцію unpack(archive_path, path_to_unpack), 
яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.

Функція нічого не повертає.
'''

import shutil

archive_path = r"E:\Git_Files\Mycode\Python\Autocheck\Module_6\folder\backup_folder.zip"

path_to_unpack = r"E:\Git_Files\Mycode\Python\Autocheck\Module_6\folder1"

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

unpack(archive_path, path_to_unpack)