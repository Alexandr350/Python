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

    @staticmethod
    def evolve():
        return 1

    def degrade(self):
        if self.S <= 0:
            print("Конец поля")
        else:
            self.S -= 1

    def count_moves(self, x2, y2):
        step = 0
        step += abs(self.X - x2)
        step += abs(self.Y - y2)
        print(step)


T1 = Turtle()
T1.go_up(4)
T1.go_left(6)
print(T1.Y, T1.X)
T1.go_left(T1.evolve())
print(T1.Y, T1.X)
T1.count_moves(2, 5)