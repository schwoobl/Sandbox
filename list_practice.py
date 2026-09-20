personnel_files = []
employee_data = []

#This program lets you enter personnel data into a list and then reads the contents of the list back
while True:
    print('Please enter the last name and first name (Or enter nothing to stop): ') #main loop
    employee = input('>')
    if employee == '': #breaks out of the loop and skips to the for loop
        break
    employee_data += [employee]
    while len(employee_data) != 4:
        print('Enter data: ')
        employee = input('> ')
        employee_data += [employee]
    personnel_files += [employee_data]
    employee_data = []
    
print('Current personnel on file: ')
for i in personnel_files:
    print('   ' + str(i))