import shutil

archive_path = r"E:\Git_Files\Mycode\Python\Autocheck\Module_6\folder\backup_folder.zip"

path_to_unpack = r"E:\Git_Files\Mycode\Python\Autocheck\Module_6\folder1"

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

unpack(archive_path, path_to_unpack)