#Make an array of numbers
f = open("input.txt", "r")
f = f.read().strip().split("\n")
f = [int(x) for x in f]
last = 0
counter = 0

# get the sum of the 3 numbers next to eachother
sumed = [sum(f[i:i+3]) for i, _ in enumerate(f)]

#same as 1
for i in sumed:
    if i > last:
         counter += 1
    last = i


print(counter-1)
