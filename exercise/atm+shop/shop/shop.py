import json

def shop():
    with open('./data/product_list.txt') as f:
        products = dict(json.load(f))
    shopping_list = []
    total = 0
    while True:
        for k, v in products.items():
            print(k, v)
        choice = input("Please choose what you want to buy:")
        if choice == 'pay':
            print('You have bought sth below stiff:')
            for i in shopping_list:
                print('\t', i)
            return total
        if choice == 'del':
            cho = input('Please imput you need del product:')
            if cho in products.keys():
                shopping_list.remove(products[cho])
                total -= products[cho][1]
        if len(choice) == 0:continue
        if choice in products.keys():
            shopping_list.append(products[choice])
            total += products[choice][1]
        else:
            continue
        print("\033[34;1mAdding %s to shopping list, total %s \033[0m" % (products[choice][0], total))
