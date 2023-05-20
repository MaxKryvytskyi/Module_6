import re
path = "06_05.csv"

def get_cats_info(path):
    list_cat = []
    dictionary = {"id" : None, "name" : None, "age" : None}
    with open(path, 'r') as fh:
        for items in fh:
            items.split(",")
            val = re.sub(r"\n", "", items)
            s = val.split(",")
            dictionary.update({"id": s[0]})
            dictionary.update({"name": s[1]})
            dictionary.update({"age": s[2]})
            list_cat.append(dictionary)
            dictionary = {}

        return list_cat

get_cats_info(path)
            
            
    