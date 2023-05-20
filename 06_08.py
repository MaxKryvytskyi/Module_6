
source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output = '06_08.csv'

def save_applicant_data(source, output):
    with open(output, 'w') as fn:
        for arguments in source:
            name = arguments["name"]
            specialty = arguments["specialty"]
            math = arguments["math"]
            lang = arguments["lang"]
            eng = arguments["eng"]
            fn.write(f"{name},{specialty},{math},{lang},{eng}\n")

save_applicant_data(source, output)