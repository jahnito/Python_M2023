class Table():
    def __init__(self):
        self.board = [[None for j in range(3)] for i in range(3)]
    
    def render_board(self):
        for i in self.board:
            for j in i:
                print('|', ' ' + j + ' ' if j else '   ', sep='', end='')
            print('|')

if __name__ == '__main__':
    t1 = Table()
    t1.board[1][1] = "X"
    t1.render_board()

