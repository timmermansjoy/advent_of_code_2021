from itertools import permutations

def readInput8(filename):
    with open(filename) as f:
        return [[y.split() for y in x.strip('\n').split(" | ")] for x in f.readlines()]

f = readInput8("day8/input8a.txt")

display = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

output = 0
origin = 'abcdefg'
r = ""
for left, right in f:
    for p in permutations(origin):
        scramb = "".join(p)
        code = {x: y for x,y in zip(origin,scramb)}
        ll = [ "".join(sorted([ code[s] for s in x ])) for x in left ]
        r = [ "".join(sorted([ code[s] for s in y ])) for y in right ]
        if sum([1 if i in display.keys() else 0 for i in ll ])==len(ll) and sum([1 if o in display.keys() else 0 for o in r ])==len(r):
            break
    # output value
    value = int("".join(str(display[num]) for num in r))
    output += value

print(output)
