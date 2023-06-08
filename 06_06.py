'''
Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, 
яка приймала на вхід список з інгредієнтами рецепта.

Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт 
у файлі та повертатиме знайдений рецепт у вигляді словника певної форми.

У вас є файл, який містить рецепти у вигляді:

60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). 
Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, 
а потім через кому, йде перелік інгредієнтів рецепта.

Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної страви що шукається. 
Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.

Де параметри функції:

path — шлях до файлу.
search_id — первинний ключ MongoDB для пошуку рецепта
Вимоги:

Використовуйте менеджер контексту with для читання з файлу
Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
Приклад: для файлу, вказаного вище, виклик функції у вигляді

get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese 
і повернути результат у вигляді словника такої структури:

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}
'''

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



        
            
            
                