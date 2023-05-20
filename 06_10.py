
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}

path = '06_10.csv'

def save_credentials_users(path, users_info):
    with open(path, "wb") as file:
        for username, password in users_info.items():
            strt = username + ":" + password + "\n"
            result = strt.encode()
            file.write(bytes(result))



print(save_credentials_users(path, users_info))

