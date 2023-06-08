'''
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл 
output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''

import re
source = "06_07[0]"

output = "06_07[1]"


def sanitize_file(source, output):
    with open(source, "r+") as f:
        text_num = f.read()
        text = re.search(r"\d+", text_num)
        text1 = text_num.replace(text.group(), "")
        with open(output, "w+") as fn:
            fn.write(text1)

        

sanitize_file(source, output)
    
    
    