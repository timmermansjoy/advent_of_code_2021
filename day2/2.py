f = open("input.txt", "r")
f = f.read().strip().split("\n")

test = [i.split() for i in f]

placement = {"horizontal": 0, "depth": 0, "aim": 0}


for i, item in enumerate(test):

    direction, number = item[0], item[1]

    if direction == "up":
        placement["aim"] -= int(number)
    elif direction == "down":
        placement["aim"] += int(number)
    elif direction == "forward":
        placement["horizontal"] += int(number)
        placement["depth"] += int(number) * placement["aim"]


print(placement["horizontal"] * placement["depth"])
