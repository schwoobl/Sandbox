#Beginning Message Calculator
print('This is a calculator.')
print('What do you want to do?')

operation = input()

#Function to request and store the number input
def numberInput():
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))
    return num1, num2

#Check the operation and perform the calculation based on the input from numberInput
    
if operation == 'Add':
    num1, num2 = numberInput()
    add_result = num1 + num2
    print('Result: ', add_result)
elif operation == 'Subtract':
    num1, num2 = numberInput()
    sub_result = num1 - num2
    print('Result: ', sub_result)
elif operation == 'Multiply':
    num1, num2 = numberInput()
    mul_result = num1 * num2
    print('Result: ', mul_result)
elif operation == 'Divide':
    num1, num2 = numberInput()
    div_result = num1 / num2
    print('Result: ', div_result)
else:
    print('Invalid input')
