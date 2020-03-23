from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        value = randint(1, self.sides)
        return value

    def count_roll(self, counts):
        count = 1
        while count <= counts:
            print("The " + str(count) + " time is " + str(self.roll_die()))
            count += 1


six_die = Die()
six_die.count_roll(10)

print("============================================")

ten_die = Die(10)
ten_die.count_roll(10)

print("============================================")

ten_die = Die(20)
ten_die.count_roll(10)
