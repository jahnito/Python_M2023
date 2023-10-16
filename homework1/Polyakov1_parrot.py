from random import choice

class Parrot():
    def __init__(self, voice='Привет, друзья!'):
        self.voice = [voice]

    def say(self, c=1):
        print(f'{choice(self.voice)} ' * c)

    def learn(self, say):
        self.voice.append(say)


p1 = Parrot('Гав!')
p2 = Parrot('Мяу!')

p1.learn("Hello")
p1.learn("Privet")


p1.say()

p1.say(3)
