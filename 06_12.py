import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']

def encode_data_to_base64(data):
    list_base64 = []
    for i in data:
        base64_data = base64.b64encode(i.encode('utf-8'))
        base64_data = base64_data.decode('utf-8')
        list_base64.append(base64_data)
    return list_base64

print(encode_data_to_base64(data))
        