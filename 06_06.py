# import re
path = "06_06.csv"
search_id = "60b90c3b13067a15887e1ae4"


# def get_recipe(path, search_id):
#     dictionary = {
#         "id": "None",
#         "name": "None",
#         "ingredients": [

#         ]
# }
#     with open(path, "r") as fh:
#         for i in fh:
#             a = re.search(search_id, i)
#             if a is not None:
#                 a = i.split(",")
#                 print(a)
#                 dictionary.update({"id" : a.pop(0)})
#                 dictionary.update({"name" : a.pop(0)})
#                 dictionary.update({"ingredients" : a})
#                 return dictionary
#         return None
# print(get_recipe(path, search_id))

def get_recipe(path, search_id):
    with open(path, 'r') as f:
        recipes = f.readlines()
    for reciep in recipes:
        reciep = reciep.replace('\n', '')
        if search_id in reciep:
            recipe_l = reciep.split(',') 
            print(recipe_l)
            return {'id':recipe_l[0], 'name':recipe_l[1], 'ingredients':recipe_l[2:]}
print(get_recipe(path, search_id))



        
            
            
                