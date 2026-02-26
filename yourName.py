#This program says hello and asks for my name and age.

print('Hello world!')
print("What is your name?")
my_name = input("Your name: ") #User-Eingaben die mit Input() gespeichert werden, werden als STRING gespeichert!
print("Hello " + my_name + ", it's good to meet you!")
print("The length of your name is " + str(len(my_name))) #len() gibt die Anzahl der Zeichen in einer Variable als integer wider, daher muss das Ergebnis mit str() in einen String verwandelt werden, um im Print() benutzt zu werden.
print("What is your age?")
my_age = input("Your age: ")
print("You will be " + str(int(my_age) + 1) + " in a year.") #Um auszurechnen, wie alt ich in einem Jahr bin, muss der in my_age als STRING gespeicherte Wert mit int() in einen Integer umgewandelt werden, damit python mit dem Wert rechnen kann. Anschließend muss dieser Wert mit str() wieder in einen String umgewandelt werden, um ihn im print() Statement auszugeben.
#todo Fortführung der Konversation mit If-statements und mehr input feldern