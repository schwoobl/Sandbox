try:     
    guess = int(input(">"))     #Takes the players input and converts to an integer
except:
    print(": Please enter a valid number!")
finally:
    guess = int(input(">"))