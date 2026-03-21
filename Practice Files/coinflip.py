# import random
# for i in range(100):  # Perform 100 coin flips.
#     if random.randint(0, 1) == 0:
#         print('H', end=' ')
#     else:
#         print('T', end=' ')
# print()  # Print one newline at the end.


# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"

# for letter in message:
#     if letter == "x":
#         print(" ", end=" ")
#     else:
#         print(letter, end=" ")

# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"

##exercise 1
# def replacement():
#     new_message = ""
#     for letter in message:
#         if letter == "T":
#             new_message += " - "
#         else:
#             new_message += letter + " "
#     return new_message
# new_message = replacement()
# print(new_message)

##exercise 2
# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# counter = 0
# for letter in message:
#     if letter == "H":
#         counter -= 1
# print(counter)

##exercise 3
# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# new_message = ""
# for letter in message:
#     if letter == "x":
#         new_message += " "
#     elif letter == "T":
#         new_message += "*"
#     else:
#         new_message += letter
# print(new_message)

##exercise 4
# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# new_message = ""

# for letter in message:
#     if letter != "H":
#         new_message += ""
#     else:
#         new_message += letter

# print(new_message)

#exercise 5

message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
counter = 0 
for letter in message:
    if counter == 5:
        print(letter)
        counter = 0
    else:
        print(letter,end="")
        counter += 1