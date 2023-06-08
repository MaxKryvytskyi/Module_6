'''
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, 
створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. 
Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
'''

import re
path = "06_10.csv"

def get_credentials_users(path):
    with open(path, "rb") as file:
        f = file.read()
        f = f.decode()
        f = re.sub("\n", " ", str(f))
        result = []
        result += f.split()
        return result 
            
# print(get_credentials_users(path))

with open("06_12.csv", "w+") as fh:
    fh.write(str(get_credentials_users(path)))