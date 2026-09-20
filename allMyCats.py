# print('Enter the name of cat 1: ')
# cat_name_1 = input()
# print('Enter the name of cat 2: ')
# cat_name_2 = input()
# print('Enter the name of cat 3: ')
# cat_name_3 = input()
# print('Enter the name of cat 4: ')
# cat_name_4 = input()
# print('Enter the name of cat 5: ')
# cat_name_5 = input()
# print('The cat names are: ' + cat_name_1 + ', ' + cat_name_2 + ', ' + cat_name_3 + ', ' + cat_name_4 + ' & ' + cat_name_5) 

cat_names = []

while True:
    print('Enter the name of cat Nr. ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop.): ')
    name = input('>')
    if name == '':
        break
    cat_names = cat_names + [name] #Putting the variable in brackets adds the value in the variable to the list
print('The cat names are: ')
for name in cat_names:
    print('  ' + name)
