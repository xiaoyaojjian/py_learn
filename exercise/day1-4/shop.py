
salary = int(input("\033[33;0mPlease input you salary:\033[0m"))

products = [
    ['Iphone', 5800],
    ['MacPro', 12000],
    ['NB Shoes', 680],
    ['Cigarate', 120000],
    ['MX4', 2500]
]
choice_list = []
choice_list.extend(range(len(products)))
print(choice_list)
shopping_list = []

while True:
    for p in products:
        print(products.index(p), p[0],':',p[1])
    choice = input("Please choose what you want to buy:")
    if choice == 'quit':
        print('You have bought sth below stiff:')
        for i in shopping_list:
            print('\t', i)
        exit('Goodbye')
    if len(choice) == 0:continue
    if int(choice) in choice_list:
        pro = products[int(choice)]
    else:
        continue
    if salary >= pro[1]:
        salary -= pro[1]
        shopping_list.append(pro)
        print("\033[34;1mAdding %s to shopping list, you have %s left\033[0m" % (pro[0], salary))
    else:
        print("The price of %s is %s, yet you current blence is %s, so try another one!" % (pro[0], pro[1], salary))
