# import lesson_package.utils
# from lesson_package import utils
from lesson_package.utils import say_twice
from termcolor import colored

print ('test')
print(__name__)

print(colored('test', 'red'))
# print(help(colored))

# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
r = say_twice('hello')

print(r)