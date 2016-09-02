# List:
"""
my_list = [1, 2, 3, 4, 5]
my_list[:3]  # start from index 0 to 2 excluding 3
my_list[3:]  # start from index 3 to the end
letters = ['a', 'b', 'c']
letters.append('d')  # Append additional letters
"""
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")  # Use index() to find "duck" and return the index
animals.insert(duck_index, "cobra")  # Insert at the index position
print(animals)  # Return ['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']
animals.remove("aardvark")  # Remove an item from the list


# List with for-loop:
my_list = [1, 9, 3, 8, 5, 7]
for number in my_list:  # Loop every item in the list
    print(2 * number)

start_list = [5, 3, 1, 2, 4]
square_list = []  # Empty list

for numbers in start_list:
    square_list.append(numbers ** 2)
    square_list.sort()  # Sort the item in th list in a increasing manner
print(square_list)


# Dictionaries:
d = {'key1': 1, 'key2': 2, 'key3': 3}  # By looking at keys instead of index

residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
print(residents['Puffin'])  # Prints Puffin's room number

menu = {}  # Empty dictionary
menu['Chicken Alfredo'] = 14.50  # Adding new key-value pair
print(menu['Chicken Alfredo'])
del menu['Chicken Alfredo']  # Delete key-value pair
menu['Chicken Alfredo'] = 5  # Assign new value

# String looping:
for letter in "Codecademy":
    print(letter)  # Print each character line by line
    print()  # Empty lines to make the output pretty

word = "Programming is fun!"
for letter in word:
    if letter == "i":  # Only print out the letter i
        print(letter)


# List and dictionary exercise 1:
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],  # Assign a new list to 'pouch' key
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby',
                           'three-toed sloth']  # Add a key 'burlap bag' and assigning a list to it

inventory['pouch'].sort()  # Sort the list found under the key 'pouch' alphabetically
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove("dagger")  # Delete an item from the list under the dictionary
inventory['gold'] = 550


# List and dictionary exercise 2:
webster = {  # The value could also be string
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print(webster[key])  # Loop over the dictionary


# List and dictionary exercise 3:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
    if number % 2 == 0:  # Return those that can be divided by 2
        print(number)


# List and dictionary exercise 4:
def fizz_count(x):
    count = 0
    for item in x:
        if item == 'fizz':
            count += 1  # Count the total number
    return count


# List and dictionary exercise 5:
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
total = 0
for key in prices:
    print(key)
    print("price: %s" % prices[key])  # Return the result in string type
    print("stock: %s" % stock[key])
    print(prices[key] * stock[key])
    total += prices[key] * stock[key]
    print(total)


# List and dictionary exercises 6:
shopping_list = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total_bill = 0
    for item in food:
        if stock[item] > 0:  # if there is an item in stock
            total_bill += prices[item]
            stock[item] += - 1  # subtract the count by 1 each time
    return total_bill
