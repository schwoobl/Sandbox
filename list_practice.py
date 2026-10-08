personnel_files = []
employee = []


#This program lets you enter personnel data into a list and then reads the contents of the list back
while len(personnel_files) != 4:
    print('Please enter the last name and first name (Or enter nothing to display personnel files): ') #main loop
    employee = input('>')
    print(f'Appending {employee} to the files')
    if employee == '': #breaks out of the loop and skips to the for loop
        break
    personnel_files.append(employee)
    
print('Current personnel on file: ')
for name in personnel_files:
    print('   ' + str(name))