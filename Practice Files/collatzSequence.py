# def collatz(number):
#     if number % 2 == 0:
#         number = number // 2
#         print(number)
#     else:
#         number = 3 * number + 1
#         print(number)
#     return number

# user_input = int(input("Please enter a number:"))

# while True:
#     collatz(user_input)
#     print(collatz(user_input), sep=", ")
#     return collatz()

def collatz(local_number):
    if local_number % 2 == 0:
        result = local_number // 2
    else:
        result = 3 * local_number + 1
    
    print(result, end=' ')  # prints on one line
    return result


global_number = int(input("Enter a number: "))

print(global_number, end=' ')  # print starting number

while global_number != 1:
    global_number = collatz(global_number)