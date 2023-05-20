
path = '06_02.csv'
def read_employees_from_file(path):
    fh = open(path, 'r')
    all_file = fh.read()
    a = all_file.strip('\n').split('\n')
    fh.close()
    return a
print(read_employees_from_file(path))





