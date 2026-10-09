shopping_list = {}

while True:
    print('Please add items to your shopping list: (Or enter nothing to display the list')
    item = input({'>'})
    if item == '':
        break 
    shopping_list.update(item)
    item = ''
print('Things to buy: ')
for k, v in shopping_list:
    print(k, v)
    