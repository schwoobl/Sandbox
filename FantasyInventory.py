inventory = {'gold' : 78, 'torch' : 2, 'dagger' : 1, 'rope' : 1, 'arrows' : 1, 'bow' : 1}

def display_inventory():
    print('Current inventory includes: ', end="")
    for item, number in inventory.items(): # loops through the dictionary and assigns the first index to the dictionary KEY and the second index to the dictionary value
        print(item + ': ' + str(number)) # prints the items in the dictionary (str() to conver the integer value)
    print('Total number of items in inventory: ' + str(sum(inventory.values()))) # since the dict values are all integers we use sum() to add them all up
    
display_inventory()