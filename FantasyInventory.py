# Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.
# 
# Write a function named display_inventory() that would take any possible “inventory” and display it like the following:
# 
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
# Hint: You can use a for loop to loop through all keys in a dictionary.


inventory = {'gold coin' : 78, 'torch' : 2, 'dagger' : 1, 'rope' : 1, 'arrows' : 1, 'bow' : 1}

def display_inventory():
    print('Current inventory includes: ')
    for item, number in inventory.items(): # loops through the dictionary and assigns the first index to the dictionary KEY and the second index to the dictionary value
        print(item + ': ' + str(number)) # prints the items in the dictionary (str() to convert the integer value)
    print('Total number of items in inventory: ' + str(sum(inventory.values()))) # since the dict values are all integers we use sum() to add them all up
    
display_inventory()

# List-to-Dictionary Loot Conversion
# 
# Imagine that the same fantasy video game represents a vanquished dragon’s loot as a list of strings,
# like this:
# 
# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named add_to_inventory(inventory, added_items).
#
# The inventory parameter is a dictionary representing the player’s inventory
# (as in the previous project) and the added_items parameter is a list, like dragon_loot.
# 
# The add_to_inventory() function should return a dictionary that represents the player’s updated inventory.
#
# Note that the added_items list can contain multiples of the same item.
# Your code could look something like this:
# 
# def add_to_inventory(inventory, added_items):
#     # Your code goes here.
# 
# inv = {'gold coin': 42, 'rope': 1}
# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = add_to_inventory(inv, dragon_loot)
# display_inventory(inv)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inv, added_items):
    inventory.update()