class LampRow():
    colors = {0: '_', 1: '*', 2: 'o'}

    def __init__(self, count_lamps=8):
        self.count_lamps = count_lamps
        self.__state = 0

    def __set_state(self, nstate):
        if len(nstate) == self.count_lamps:
            self.__state = int(nstate)
        else:
            self.__state = 0
    
    def __get_state(self):
        return self.__state

    def show(self):
        print(' '.join([self.colors.get(int(i)) for i in f'{str(self.__state):0{self.count_lamps}}']))

    state = property(__get_state, __set_state)


if __name__ == '__main__':
    lamps = LampRow(6)
    lamps.show()
    lamps.state = '102102'
    print(lamps.state)
    lamps.show()
    lamps.state = '10201010'
    print(lamps.state)
    lamps.show()
