'''
Ячейки игрового поля нумеруем по нумпаду для дуобства игры:

7 8 9
4 5 6
1 2 3

'''

class Table():
    cells = {7: (0, 0), 8: (0, 1), 9: (0, 2),
             4: (1, 0), 5: (1, 1), 6: (1, 2),
             1: (2, 0), 2: (2, 1), 3: (2, 2)}

    def __init__(self):
        self.board = [[None for j in range(3)] for i in range(3)]

    def render_board(self):
        for i in self.board:
            for j in i:
                print('|', ' ' + j + ' ' if j else '   ', sep='', end='')
            print('|')

    def set_sign(self, cell, sign):
        x, y = self.cells[cell]
        self.board[x][y] = sign

    def check_cell(self, cell):
        x, y = self.cells[cell]
        if self.board[x][y]:
            print('Ячейка уже занята')
            return False
        else:
            print('Нормуль ячейка, ставим туда сигну')
            return True


class Gamer():
    win_order = ((1,5,9), (7,5,3), (1,2,3), (4,5,6),
                 (7,8,9), (1,4,7), (2,5,8), (3,6,9))

    def __init__(self, name):
        self.name = name
        self.cells = []

    def move(self, table:Table, cell, sign):
        if table.check_cell(cell):
            table.set_sign(cell, sign)
            self.cells.append(cell)
            return True
        else:
            return False
    
    def check_win(self):
        for i in self.win_order:
            if len(set(i).intersection(self.cells)) == 3:
                return True
            else:
                False


class GamerX(Gamer):
    def __init__(self, name):
        super().__init__(name)
        self.sign = 'X'
    
    def __str__(self):
        return f"Игрок идущий во имя {self.sign} по имени {self.name}"


class GamerO(Gamer):
    def __init__(self, name):
        super().__init__(name)
        self.sign = 'O'

    def __str__(self):
        return f"Игрок идущий во имя {self.sign} по имени {self.name}"


def start():
    message = '''
Выбирайте ячейку в соответствии с данной раcстановкой

| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |

Игровое поле
'''
    table1 = Table()
    gx = GamerX(input('Введите имя играющего крестиками: '))
    go = GamerO(input('Введите имя играющего ноликами: '))
    print(gx, go, sep='\n')
    print(message)
    table1.render_board()
    for i in range(9):
        if i % 2 == 0:
            gamer = gx
        else:
            gamer = go
        while True:
            while True:
                cell = input(f'Введите ячейку для игрока {gamer.name} играюшего {gamer.sign}: ')
                if cell.isdigit() and 1 <= int(cell) <= 9:
                    cell = int(cell)
                    break
                else:
                    print('Некорректное значение ячейки, допустимые значения 1-9')
            if gamer.move(table1, cell, gamer.sign):
                break
        print(message)
        table1.render_board()
        if gamer.check_win():
            print(f'Победил игрок {gamer.name}')
            break
        


if __name__ == '__main__':
    start()
