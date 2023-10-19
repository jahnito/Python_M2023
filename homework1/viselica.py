#!/usr/bin/env python3
from random import choice


class Game:
    def __init__(self, word):
        self.word = list(word)
        self.n = len(word)
        self.line = ' '.join(['_' for i in word])
        self.opened = []
        self.bad_attempt = []

    def set_line(self, char: str):
        char = char.lower()
        if len(char) > 1 or char.isdigit():
            return False
        if char in self.word and char not in self.opened:
            self.opened.append(char)
            self.line = ' '.join([i if i in self.opened else '_' for i in self.word])
            return True
        elif char in self.opened:
            return False
        else:
            self.bad_attempt.append(char)
            return False

    def check_status_win(self):
        if len(self.opened) == len(set(self.word)):
            return True
        else:
            return False
    
    def check_status_fail(self):
        if len(self.bad_attempt) == 7:
            return True
        else:
            return False

    def render(self):
        print(self.line)
        print('Попытки: ' + ', '.join(self.bad_attempt))


def start_game():
    status = None
    G = Game(choice(WORDS))
    while True:
        print(ESHAFOT[::-1][len(G.bad_attempt)])
        G.render()
        G.set_line(input())
        if G.check_status_win():
            status = True
            break
        if G.check_status_fail():
            status = False
            break
    
    if status:
        print(ESHAFOT[::-1][len(G.bad_attempt)])
        G.render()
    else:
        print(ESHAFOT[::-1][len(G.bad_attempt)])
        print('Не повезло')


WORDS = ('забота', 'семья', 'лето', 'газировка', 'печенье', 'астронафтика')
ESHAFOT = (
'''
  _____
   |  |
   o  |
  /|\ |
   |  |
  / \ |
______|''',
'''
  _____
   |  |
   o  |
  /|\ |
   |  |
    \ |
______|''',
'''
  _____
   |  |
   o  |
  /|\ |
   |  |
      |
______|''',
'''
  _____
   |  |
   o  |
  /|\ |
      |
      |
______|''',
'''
  _____
   |  |
   o  |
   |\ |
      |
      |
______|''',
'''
  _____
   |  |
   o  |
   |  |
      |
      |
______|''',
'''
  _____
   |  |
   o  |
      |
      |
      |
______|''',
'''
  _____
   |  |
      |
      |
      |
      |
______|'''

)

if __name__ == '__main__':
    start_game()
