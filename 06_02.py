path = '06_02.csv'

employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for list1 in employee_list:
        for lis in list1:
            fh.write(lis + "\n")
    fh.close()
    return path
write_employees_to_file(employee_list, path)
    
    
        
            
                
    
        
