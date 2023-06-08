'''
Є два рядки у різних кодуваннях - "utf-8" та "utf-16". 
Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), 
яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
'''


utf8_string = b'hello'

utf16_string = b'Hello Bro'

# utf8_string = b'\xd0\x9f\xd1\x80\xd1\xb8\xd0\xb2\xd0\xb5\xd1\x82!'
# utf16_string = b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'
def is_equal_string(utf8_string, utf16_string):
    str_utf8 = utf8_string.decode('utf-8')
    str_utf16 = utf16_string.decode('utf-16')
    return str_utf8 != str_utf16

print(is_equal_string(utf8_string, utf16_string))
