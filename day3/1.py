f = open("input.txt", "r")
f = f.read().strip().split("\n")

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in f:
    for jindex, j in enumerate(i):
        if j == '1':
            ones[jindex] = ones[jindex] + 1
        else:
            zeros[jindex] = zeros[jindex] + 1


gamma = []
for i, _ in enumerate(ones):
    if ones[i] > zeros[i]:
        gamma.append(1)
    else:
        gamma.append(0)

sigma = [1 - x for x in gamma]

# binary list to integer conversion
sigma = int("".join(str(i) for i in sigma),2)
gamma = int("".join(str(i) for i in gamma),2)


print(sigma)
print(gamma)
