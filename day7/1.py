f = open("day7/input.txt", "r")
f = [int(x) for x in f.read().strip().split(',')]

total_costs = []

for i in f:
    cost = sum(abs(i - j) for j in f)
    total_costs.append(cost)

print(min(total_costs))
