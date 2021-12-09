f = open("day8/input8b.txt", "r")
f = f.read().split("\n")
f = [[y.strip() for y in x.split(" | ")] for x in f]
f = [x for x in f if x != ['']]
segments = [2,4,3,7]
nums = [x[1] for x in f]
count = 0

for signal in nums:
    n = signal.split()
    for x in n:
        if len(x) in segments:
            count += 1

print(count)
