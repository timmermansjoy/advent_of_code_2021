f = open("day6/input1b.txt", "r")
f = [int(x) for x in f.read().strip().split(',')]


class fish:
    def __init__(self, age=9):
        self.age = age

    def __repr__(self):
        return str(self.age)

    def reset(self):
        self.age = 6

    def get_older(self):
        if self.age == 0:
            self.reset()
        else:
            self.age -= 1


school = [fish(age) for age in f]

for _ in range(80):
    for blub in school:
        if blub.age == 0:
            school.append(fish())
        blub.get_older()
    # print(f"After day {_}: {school}")

print(len(school))
