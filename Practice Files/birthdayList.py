birthdays = {"Mike" : "14 Sep", "Steffi" : "24 Jan", "Jan" : "13 Feb"}

while True:
    print("Enter a name (blank to quit)")
    name = input(">")
    if name == "":
        break
    
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have the birthday of " + name)
        print("What is their birthday?")

        bday = input(">")
        birthdays[name] = bday
        print("Database updated.")

