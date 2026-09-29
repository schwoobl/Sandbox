birthdays = {'Mike' : '14 Sep', 'Steffi' : '29 Jan', 'Karin' : '15 Dez'}

while True:
    print('Enter a name (Or leave blank to quit):')
    
    name = input('>')
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input('>')
        birthdays[name] = bday
        print('Database updated.')