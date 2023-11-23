class Turtle:

    def __init__(self, x=10, y=10, s=1):
        self.pos_x = x
        self.pos_y = y
        self.step = s

    def go_up(self, s):
        self.pos_y += s

    def go_down(self, s):
        self.pos_y -= s

    def go_left(self, s):
        self.pos_x -= s

    def go_right(self, s):
        self.pos_x += s

    def evolve(self):
        self.step += 1

    def degrade(self):
        if self.step - 1 <= 0:
            print('Невозможно уменьшить шаг')
            return False
        else:
            self.step -= 1
            return self.step

    def count_moves(self, x2, y2):
        count = 0
        if (self.pos_x - x2) % self.step:
            print('С таким шагом не попасть на нужную клетку')
            return False
        else:
            count += abs(self.pos_x - x2) / self.step

        if (self.pos_y - y2) % self.step:
            print('С таким шагом не попасть на нужную клетку')
            return False
        else:
            count += abs(self.pos_y - y2) / self.step

        return int(count)

    def __str__(self):
        return f'Позиция х - {self.pos_x}, Позиция y - {self.pos_y}, Шаг {self.step}'


test = Turtle(5, 1, 2)

print(test)
print(test.degrade())
print(test.count_moves(1, 2))
print(test.degrade())
test.evolve()

print(test.count_moves(1, 2))
