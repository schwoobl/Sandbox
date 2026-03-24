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

##Exercise 1: Swap characters
#Replace all "T" with "-" and print the result.
# You should use:
# a for loop
# build a new string (new_message)

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

##Exercose 2: Count characters
#Count how many "H" characters are in the message.
# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# counter = 0
# for letter in message:
#     if letter == "H":
#         counter -= 1
# print(counter)

##Exercise 3: Swap characters
# Focus: multiple conditions + string building
# Exercise 3: Swap characters
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

##Exercise 4: Only keep certain letters
# Create a new string that contains only "H" characters (remove everything else).
# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# new_message = ""

# for letter in message:
#     if letter != "H":
#         new_message += ""
#     else:
#         new_message += letter

# print(new_message)

##Exercise 5: Group output
#Print the message in chunks of 5 characters per line.


# message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"
# letter_counter = 0 
# for letter in message:
#     if letter_counter == 4:
#         print(letter, end="")
#         letter_counter = 0
#     else:
#         print(letter)
#         letter_counter += 1

#Exercise 6: Alternate case (slightly tricky)
#Alternate case (slightly tricky)
# Convert:
# every even index → lowercase
# every odd index → uppercase
# This introduces:
# range(len(message))
# indexing (message[i])

message = "xHxTxHxTxTxHxHxHxHxTxTxHxTxHxTxHxHxHxHxTxHxTxTxTxHxTxHxTxHxHxTxHxHxHxTxTxTxHxTxHxHxTxHxTxTxHxTxHxTxTxTxTxTxTxHxTxTxTxTxTxHxTxHxTxTxTxTxTxHxHxHxTxHxHxHxHxHxTxHxHxHxTxTxHxTxTxTxTxHxHxHxHxHxHxHxTxHxTxTx"

print(range(len(message),2))