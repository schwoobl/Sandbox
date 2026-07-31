#Exercise 1. Arithmetic Product and Conditional Logic

# Practice Problem: Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.
# Exercise Purpose: Learn basic control flow and the use of if-else statements. 
# Understand how code decisions change output based on a mathematical threshold.

def logic(num1, num2):

    if num1 * num2 <= 1000:
        result = num1 * num2
        print(result)
    else:
        result = num1 + num2
        print(result)

logic(30, 50)

