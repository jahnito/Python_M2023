class Pet():
    def __init__(self, name=None, age=None):
        if name:
            self.__name = name
        if age:
            self.__age = age

        if not hasattr(self, 'say'):
            raise NotImplementedError('Нельзя создать такой объект')

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    def __get_age(self):
        return self.__age

    def __set_age(self, age):
        self.__age = age

    def gettingOlder(self):
        self.__age = self.__age + 1

    name = property(__get_name, __set_name)
    age = property(__get_age, __set_age)


class Mammal(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self):
        print(f'{self.name} run!')


class Reptilia(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def crawl(self):
        print(f'{self.name} crawl!')


class Cat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__voice = 'Мяу'

    def say(self):
        print(f'{self.name}: {self.__voice}')


class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__voice = 'Гав'

    def say(self):
        print(f'{self.name}: {self.__voice}')


class Turtle(Reptilia):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__voice = 'Pff'

    def say(self):
        print(f'{self.name}: {self.__voice}')


class Snake(Reptilia):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__voice = 'Pshshsh'

    def say(self):
        print(f'{self.name}: {self.__voice}')


if __name__ == '__main__':
    pets = [ Cat('Murka', 3), Dog('Шарик', 5), Turtle('Leonardo', 45), Snake('Chaki', 2)]

    for p in pets:
        if isinstance(p, Mammal):
            p.run()
        if isinstance(p, Reptilia):
            p.crawl()
