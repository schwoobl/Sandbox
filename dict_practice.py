shopping_list = {}

while True:
    print('Please add items to your shopping list: (Or enter nothing to display the list')
    item = input('>')
    if item == '':
        break 
    print('Quantity? >')
    quantity = input('>')
    shopping_list[item] = quantity
    item = ''
print('Things to buy: ')
for k, v in shopping_list.items():
    print(k, v)
    