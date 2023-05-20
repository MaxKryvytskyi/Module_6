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
    
    
    