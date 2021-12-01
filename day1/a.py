
# f = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263""".strip().split("\n")


f = open("input.txt", "r")
f = f.read().strip().split("\n")
last = 0
counter = 0
f = [int(x) for x in f]

sumed = [sum(f[i:i+3]) for i, _ in enumerate(f)]

print(sumed)
print(f)

for i in sumed:
    if i > last:
         counter += 1
    last = i


print(counter-1)
