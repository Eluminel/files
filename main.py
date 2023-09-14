file = open("Cook_book.txt")
dishes = file.read().split("\n\n")

cook_book = {}
for dish in dishes:
    item = dish.split("\n")
    name, *ingredients = item
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

shop_list = {}
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        ingredients = cook_book[dish]
        for item  in ingredients:
            if item['ingredient_name'] in shop_list.keys():
                shop_list[item['ingredient_name']]['quantity'] += int(item['quantity']) * person_count
            else:
                shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                      'quantity': int(item['quantity']) * person_count
                }
get_shop_list_by_dishes(["Омлет", "Блины"], 3)
print(shop_list)


