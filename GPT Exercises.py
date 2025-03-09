#Print numbers
#Write a for loop to print numbers from 1 to 10
number = 0
for number in range(0, 11):
    print(number)

#Write a while loop to print numbers from 10 to 1 (in reverse).
while number > 0:
    print(number - 1)
    number -= 1

#Sum of Numbers
#Use a loop to calculate the sum of numbers from 1 to 100
total = 0
for num in range(101):
    total = total + num
print(total)

#Even and Odd Numbers
#Print even numbers between 1 and 50.
for i in range(0, 50):
    if i % 2 == 0:
        print(i)

#Print odd numbers between 1 and 50.
for i in range(0, 50):
    if i % 2 == 1:
        print(i)

#Multiplication Table
#Ask the user for a number (e.g., n = 5).
#Print the multiplication table for that number (1 to 10)
print("Give me a random number.")
number = int(input())
for number in range(0, 11):
    print(number * 2)