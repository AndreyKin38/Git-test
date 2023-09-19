from random import randint


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    @property
    def is_human_win(self):
        return self.get_winner(1)

    @property
    def is_computer_win(self):
        return self.get_winner(2)

    @property
    def is_draw(self):
        if self.get_winner(1) or self.get_winner(2):
            return False
        if self.field_status():
            return False
        return True

    def init(self):
        for i in self.pole:
            for j in i:
                j.value = 0

    def show(self):
        field = [[self[i, j] for j in range(3)] for i in range(3)]
        for row in field:
            print(*map(lambda x: x, row))
        print()

    def __bool__(self):
        if self.is_human_win or self.is_computer_win or self.is_draw:
            return False
        return True

    def field_status(self):
        lst = [i.value for row in self.pole for i in row]
        return 0 in lst

    def get_winner(self, value):
        rows = [[self[i, j] for j in range(3)] for i in range(3)]
        cols = [[self[j, i] for j in range(3)] for i in range(3)]
        diag1 = [self[i, i] for i in range(3)]
        diag2 = [self[2-i, i] for i in range(3)]

        for row in rows:
            if all(map(lambda x: x == value, row)):
                return True

        for col in cols:
            if all(map(lambda x: x == value, col)):
                return True

        if all(map(lambda x: x == value, diag1)):
            return True
        if all(map(lambda x: x == value, diag2)):
            return True

        return False

    def human_go(self):
        i = int(input())
        j = int(input())
        if not bool(self[i, j]):
            self[i, j] = self.HUMAN_X
        else:
            self.human_go()

    def computer_go(self):
        while True:
            i = randint(0, 2)
            j = randint(0, 2)
            if not bool(self[i, j]):
                self[i, j] = self.COMPUTER_O
                break

    @staticmethod
    def check_index(index):
        i, j = index
        if type(i) != int or type(j) != int or \
            not (0 <= i < 3) or not (0 <= j < 3):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.check_index(key)
        i, j = key
        self.pole[i][j].value = value


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0



game = TicTacToe()
game.init()
step_game = 0
# print(game.is_human_win)
# print(game.is_computer_win)
# print(game.is_draw)
# print(game.field_status())

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
