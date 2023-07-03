class Cassa:

    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        self.balance += X

    def count_1000(self):
        print(self.balance // 1000)

    def take_away(self, X):
        if X > self.balance:
            print("Недостаточно денег")
        else:
            self.balance -= X


C1 = Cassa()
C1.top_up(1000)
print(C1.balance)
C1.take_away(1000)
print(C1.balance)
C1.take_away(1000)
C1.top_up(3500)
C1.count_1000()