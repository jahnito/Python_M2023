import getpass


class Gamer():
    __number = None
    number_guessed = False
    attempts = 0

    def __init__(self, name):
        self.name = name
        if not self.__number:
            self.__set_number()

    def check_number(self, num: str) -> bool:
        if not num.isdigit():
            return True
        if int(num) < 999 or int(num) > 10000:
            return True
        if len(set(num)) != 4:
            return True

    def attempt_guesse(self, gamer):
        message = f'Attempt by player {gamer.name}: '
        a = input(message)
        while self.check_number(a):
            print('Invalid number')
            a = input(message)
        b = str(self.__number)
        bulls = 0
        cows = 0
        if a == b:
            self.number_guessed = True
            return f'Number guessed - {self.__number}'
        for i, n in enumerate(a):
            self.attempts += 1
            if b[i] == n:
                bulls += 1
            elif n in (b[:i] + b[i+1:]):
                cows += 1
        return f'Number of bulls {bulls} number of cows {cows}'



    def __get_number(self):
        return self.__number

    def __set_number(self):
        message = f'Enter a four-digit number {self.name}: '
        n = getpass.getpass(prompt=message)
        while self.check_number(n):
            print('Invalid number')
            n = getpass.getpass(prompt=message)
        self.__number = int(n)

    number = property(__get_number, __set_number)


def game():
    message1 = 'Input name gamer'
    gamer1 = Gamer(input(f'{message1} #1: '))
    gamer2 = Gamer(input(f'{message1} #2: '))
    while gamer1.attempts + gamer2.attempts < 20:
        print(gamer1.attempt_guesse(gamer2))
        print(gamer2.attempt_guesse(gamer1))
        if any((gamer1.number_guessed, gamer2.number_guessed)):
            break

    if gamer1.number_guessed and gamer2.number_guessed:
        print('Both players won')
    elif gamer1.number_guessed and not gamer2.number_guessed:
        print(f'Player {gamer2.name} won')
    elif not gamer1.number_guessed and gamer2.number_guessed:
        print(f'Player {gamer1.name} won')


if __name__ == '__main__':
    game()
