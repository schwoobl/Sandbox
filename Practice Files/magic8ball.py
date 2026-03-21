import random

def get_answer(answer_number):
    if answer_number == 1:
        print("It is certain")
    elif answer_number == 2:
        print("It is decidedly so")
    elif answer_number == 3:
        print("Yes")
    elif answer_number == 4:
        print("Reply hazy, try again")
    elif answer_number == 5:
        print("Ask again later")
    elif answer_number == 6:
        print("Concentrate and ask again later")
    elif answer_number == 7:
        print("My reply is no")
    elif answer_number == 8:
        print("Outlook is not so good")
    elif answer_number == 9:
        print("Very doubtful")
        
print("Ask the magic 8 ball a yes or no question")
input(">")

# r = random.randint(1,9)
# fortune = get_answer(r)
# print(fortune)

print(get_answer(random.randint(1, 9)))