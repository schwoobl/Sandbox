import random
import string

Test = "This is a testvariable with lots of different letters"

for i in Test:
    if i == "i":
        print(random.choice(string.ascii_letters).lower(), end="")
    else:
        print(i, end="")
    