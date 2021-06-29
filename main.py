from pprint import pprint

def get_cook_book_by_dishes():
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line[:-1]
            counter = f.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingredient = f.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingredient:
                    dish_items['ingredient_name'] = ingredient[0]
                    dish_items['quantity'] = ingredient[1]
                    dish_items['measure'] = ingredient[2]
                list_of_ingredient.append(dish_items)
                cook_list = {dish_name: list_of_ingredient}
                cook_book.update(cook_list)
            f.readline()
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book_by_dishes()
    shopping_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            items_list = dict([(item['ingredient_name'],
                                {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count})])
            if shopping_list.get(item['ingredient_name']):
                extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                int(items_list[item['ingredient_name']]['quantity']))
                shopping_list[item['ingredient_name']]['quantity'] = extra_item
            else:
                shopping_list.update(items_list)
    return (shopping_list)

def get_command():
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        dish_list = f.read()
        print('Наши блюда:\n', dish_list)
        dishes = input('\nВведите блюдо: ').lower().split(', ')
        # dishes = ['Фахитос']
        person_count = int(input('\nВведите количество персон: '))
        shopping_list = get_shop_list_by_dishes(dishes, person_count)
        pprint(shopping_list)

get_cook_book_by_dishes()
get_command()
get_shop_list_by_dishes()
