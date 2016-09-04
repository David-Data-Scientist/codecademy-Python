from random import randint

# Removing elements:
n = [1, 3, 5, 7]
n.pop(0)  # Remove the first item in the list here using index
n.remove(3)  # Another way to do it using the actual value
del (n[0])  # Alternative way to do it using the index
print(n)  # => [7]


# Range function:
"""
range(stop)  # Start from zero to stop excluded
range(start, stop)  # Start from the number 'start' to 'stop', excluded
range(start, stop, step)  # Start from the number 'start' to 'stop', with step length 'step'
"""
range(6)  # => [0,1,2,3,4,5]
range(1, 6)  # => [1,2,3,4,5]
range(1, 6, 3)  # => [1,4]


# Two ways to iterate over a list in a function:
lists = [3, 5, 7]
for item in lists:
    print(item)

for i in range(len(lists)):
    print(lists[i])


def total(numbers):  # Sum the numbers by iterating the list
    result = 0
    for index in range(len(numbers)):
        result += numbers[index]
    return result


# Using two lists as two arguments in a function
a = [1, 2, 3]
b = [4, 5, 6]


def join_lists(x, y):  # Combine two lists together
    return x + y

print(join_lists(a, b))  # => [1, 2, 3, 4, 5, 6]


# Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(list_of_lists):  # Expand the list of the list
    results = []
    for numbers in list_of_lists:
        for num in numbers:
            results.append(num)
    return results

print(flatten(n))  # => [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Battle ship game：
"""
This ship game is a simplified, one-player version of the classic board game Battleship.
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid.
The player will have 4 guesses to try to sink the ship.
"""
board = []
for i in range(5):  # Return 5 rows of ['O', 'O', 'O', 'O', 'O']
    board.append(["O"] * 5)


def print_board(boards):  # Return 5 rows of "O O O O O"
    for row in boards:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)


def random_row(boards):  # Randomly return the integer between zero and len(boards)-1 (4)
    return randint(0, len(boards) - 1)


def random_col(boards):
    return randint(0, len(boards[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    guess_row = int(input("Guess Row:"))  # In python 2.x is raw_input()
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or \
                (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print("Turn", turn + 1)
    if turn == 3:
        print("Game Over")
    print_board(board)
