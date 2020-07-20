class Person:
    def __init__(self, name):
        self.name = name
        print(self.name)
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(5)
    def run(self, num):
        print('run' * num)
    def __del__(self):
        print('good bye')


person = Person('Mike')
person.say_something()
del person
print('#################')

def person(name):
    if name == 'A':
        print('hello')

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

baby = Baby()
adult = Adult()

class Car:
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model = 'Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

print('##############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('##############')
tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.model)
print(tesla_car.enable_auto_run)
tesla_car.auto_run()
tesla_car.run()

class People:
    def talk(self):
        print('talk')

class Bycycle:
    def run(self):
        print('run')

class PeopleRobot(People, Bycycle):
    def fly(self):
        print('fly')

pr = PeopleRobot()
pr.talk()
pr.run()
pr.fly()