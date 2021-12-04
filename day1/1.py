f = open("input.txt", "r")
f = f.read().strip().split("\n")
last = 0
counter = 0

for i in f:
    if i > last:
         counter += 1
    last = i


print(counter)
