import numpy as np


f = open("day5/input.txt", "r")
f = f.read().strip()
f = f.replace("->", "\n")
f = f.split()

# parse the input
lines = [[f[i], f[i+1]] for i in range(0,len(f),2)]
for i, line in enumerate(lines):
    for j, point in enumerate(line):
        lines[i][j] = point.split(",")
        lines[i][j] = [int(x) for x in lines[i][j]]



# Take only horizontal or vertical lines
right_lines = [i for i in lines if i[0][0] == i[1][0] or i[0][1] == i[1][1]]
right_lines = np.array(right_lines)


# place the line on the field
max = np.amax(right_lines) +1
field = np.zeros((max,max))
for line in right_lines:
    x1, y1 = line[0][0], line[0][1]
    x2, y2 = line[1][0], line[1][1]
    if x1 == x2:
        if y1 < y2:
            field[x1, y1:y2+1] += 1
        else:
            field[x1, y2:y1+1] += 1
    elif y1 == y2:
        if x1 < x2:
            field[x1:x2+1, y1] += 1
        else:
            field[x2:x1+1, y1] += 1


total = (field >= 2).sum()

print(total)
