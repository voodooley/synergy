class Cash:

    def __init__(self, csh=1000):
        self.cash = csh

    def top_up(self, count):
        self.cash += count
        return f'В кассе {self.cash}'

    def count_1000(self):
        return self.cash // 1000

    def take_away(self, count):
        if count > self.cash:
            return 'Ошибка! В кассе недостаточно денег'
        else:
            self.cash -= count
            return f'В кассе {self.cash}'

    def __str__(self):
        return f'В кассе {self.cash}'


cash = Cash()

print(cash)

print(cash.top_up(333))
print(cash.count_1000())
print(cash.take_away(1550))
