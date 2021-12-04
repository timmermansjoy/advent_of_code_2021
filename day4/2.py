import re

f = open("day4/input.txt", "r")
f = f.read().strip().split("\n\n")


given_numbers = f[0].split(",")
given_numbers = [int(i) for i in given_numbers]



boards = f[1:]
boards = [x.split("\n") for x in boards]
boards = [[re.sub(' +', ' ', row) for row in board] for board in boards]
boards = [[row.split(' ') for row in board] for board in boards]
boards = [[[int(z) for z in x if z != ""] for x in y] for y in boards]


test = []

def horizontal(board):
    return any(all(x == '' for x in i) for i in board)


def vertical(board):
    return any(all(x == '' for x in i) for i in zip(*board))

for search_number in given_numbers:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == search_number:
                    boards[i][j][k] = ''

        h = horizontal(board)
        v = vertical(board)

        if (h or v) and i == 53:
            test.append(i)
            board = [[x for x in row if x != ''] for row in board]
            board = [x for x in board if x != []]

            sum = 0
            for row in board:
                for num in row:
                    sum += num

            print(sum*search_number)
            #Take first number



# look at what numer is last seen
seen = []
for i in test:
    if i not in seen:
        seen.append(i)

print(seen)
