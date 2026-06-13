import sys

while True:

    #Beginning Message Calculator
    print('Welcome to this simple calculator.')
    print('What do you want to do? Type "+", "-", "*" or "/", to perform the respective operations or type "Quit" to exit.')

    operation = input()

    #Function to request and store the number input
    def numberInput():
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        return num1, num2

    #Check the operation and perform the calculation based on the input from numberInput
        
    if operation == 'Quit'.strip().lower():
        sys.exit()
    try:
        if operation == '+'.strip().lower():
            num1, num2 = numberInput()
            add_result = num1 + num2
            print('Result: ', add_result)
    except:
        ValueError
        print("Please enter a valid number")
    try:
        if operation == '-'.strip().lower():
            num1, num2 = numberInput()
            sub_result = num1 - num2
            print('Result: ', sub_result)
    except:
        ValueError
        print("Please enter a valid number")
        if operation == '*'.strip().lower():
            num1, num2 = numberInput()
            mul_result = num1 * num2
            print('Result: ', mul_result)
    try:
        if operation == '/'.strip().lower():
            num1, num2 = numberInput()
            div_result = num1 / num2
            print('Result: ', div_result)
    except:
        ValueError
        print("Please enter a valid number")

        # else:
        #     print('Invalid input')
