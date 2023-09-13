file = open("Cook_book.txt")
dishes = file.read().split("\n\n")

cook_book = {}
for dish in dishes:
    item = dish.split("\n")
    name, *ingredients = item
# переделать
    _, *ingredients = ingredients
    cook_book[name] = []
    for ingredient in ingredients:
        elements = ingredient.split("|")
        cook_book[name].append(
            {
                "ingredient_name": elements[0],
                "quantity": elements[1],
                "measure": elements[2]
            }
        )
print(cook_book)

# def get_shop_list_by_dishes(dishes, person_count):
#     dishes = cook_book.keys()
#     shop_list = {}
#     for dishes, ingredients in cook_book.items():
#         a = ingredients[1] * person_count
#     shop_list =
