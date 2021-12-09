import numpy as np


f = open("day6/input1b.txt", "r")
f = [int(x) for x in f.read().strip().split(',')]
print(len(f))

ages = np.zeros(9)


for i in f:
    ages[i] += 1


for _ in range(256):
    ages = np.roll(ages, -1)
    ages[6] += ages[8]

print(sum(ages))
