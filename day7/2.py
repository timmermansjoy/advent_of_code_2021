f = open("day7/input.txt", "r")
f = [ int(h) for h in f.readlines()[0].split(",") ]

least_cost =  min(sum(((abs(j-i)+1)*abs(j-i))//2 for j in f) for i in f)

print(least_cost)
