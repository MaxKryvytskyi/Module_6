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