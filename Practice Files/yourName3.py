name = ''
count = 0
while name != 'your name':
    print('Please type your name.')
    name = input('>')
    count = count + 1
    if count >= 3 and name != 'your name':
        print("Read the instructions VERY carefully!")
print('Thank you!')
