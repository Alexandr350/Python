class Turtle:

    def __init__(self):
        self.X = 0
        self.Y = 0
        self.S = 0

    def go_up(self, S):
        self.Y += S

    def go_down(self, S):
        self.Y -= S

    def go_left(self, S):
        self.X += S

    def go_right(self, S):
        self.X -= S

    def evolve(self):
        self.S += 1

    def degrade(self):
        if self.S <= 0:
            print("Ошибка. Шаг <= 0")
        else:
            self.S -= 1

    def count_moves(self, x2, y2, S):
        step = 0
        step += abs(self.X - x2)
        step += abs(self.Y - y2)
        if S == 0:
            print('Черепашка стоит на месте')
        else:
            step_result = step / S
            print("Количество шагов до цели %.1f" % step_result)


T1 = Turtle()
T1.evolve()
T1.go_up(T1.S)
T1.go_left(T1.S)
T1.go_left(T1.S)
print("Местоположение черепашки ({0}:{1}) ".format(T1.X, T1.Y))
print("Цель ({0}:{1}), Шаг - {2}".format(6, 5, T1.S))
T1.count_moves(6, 5, T1.S)