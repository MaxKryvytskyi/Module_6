import shutil


employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}

file_name = "file.bin"

path = r"E:\Git_Files\Mycode\Python\Autocheck\Module_6\folder"
 
def create_backup(path, file_name, employee_residence):
    with open (path + "\\" + file_name, 'wb') as file:
        for name, val in employee_residence.items():
            file.write(f"{name} {val}\n".encode())

    archive_name = shutil.make_archive('folder\\backup_folder', 'zip', 'folder')
    return archive_name
create_backup(path, file_name, employee_residence)