import re 


def total_salary(path):
    fh = open(path, 'r')
    first_two_symbols = fh.read()
    numbers = re.findall('\d+', first_two_symbols)
    print(numbers)
    sum = 0
    for num in numbers:
        sum += float(num)
    fh.close()
    return sum
        
print(total_salary('06_01.csv'))
        
            