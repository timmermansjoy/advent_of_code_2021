f = open("input.txt", "r")
f = f.read().strip().split("\n")

ones = [0 for i in enumerate(f[0])]
zeros = [0 for i in enumerate(f[0])]


for index ,i in enumerate(f):
    for jindex, j in enumerate(i):
        if j == '1':
            ones[jindex] = ones[jindex] + 1
        else:
            zeros[jindex] = zeros[jindex] + 1

o2 = f
popped = o2
counter = 0
while len(o2) > 1:
    print(o2)
    if ones[counter] == zeros[counter] or ones[counter] > zeros[counter]:
        for i, item in enumerate(o2):
            if item[counter] == '0':
                popped.append(item)
                o2.pop(i)
                counter = 0
    elif ones[counter] < zeros[counter]:
        for i, item in enumerate(o2):
            if item[counter] == '1':
                popped.append(item)
                o2.pop(i)
            counter = 0
    counter += 1


print(o2)

# o2 = int("".join(str(i) for i in o2),2)
# Co2 = int("".join(str(i) for i in Co2),2)
