print('xxxx')
# コメントアウト
s = 'aaaaaaaa' \
    + 'bbbbbbb'
print(s)
# 80文字以上は分けるべきらしい
def say_something():
    print('hi')

say_something()

def what_is_this(color):
    print(color)

what_is_this('red')

def add_num(a: int , b: int) -> int:
    return a + b

r = add_num(12, 33)
print(r)

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef', drink='beer', dessert='ice')

def test_func(x, l=[]):
    l.append(x)
    return  l

y = [1,2,3]
r = test_func(100, y)
print(r)

e = test_func(100)
print(e)

e = test_func(100)
print(e)

def say_something(*args):
    print(args)
    for arg in args:
        print(arg)

t = ('Mike', 'Nance')
say_something('Hi', *t)

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k,':', v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ise'
}
menu(**d)

def outer(a,b):
    def innner():
        return a + b

    return innner
f = outer(1,2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.1415926)

print(ca1(10))
print(ca2(10))


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        print('func:', func.__name__)
        print('kwargs:', kwargs)
        print('args', args)
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('中間')
        print('中間')
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return  a + b

r = add_num(10, 20)
print(r)

@print_more
@print_info
def del_num(c,d):
    return c - d

g = del_num(50, 30)
print(g)

l = ['Mon', 'tue', 'Wed', 'thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
# sample_func = lambda word: word.capitalize()
# change_words(l, sample_func)
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

l = ['Good morning', 'Goot afternoon', 'Good night']

for i in l:
    print(i)

print("##################")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print("##################")
print(next(g))
print("##################")
print(next(g))

t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)


r = []
for i in t:
    r.append(i)
print(r)

r = [i for i in t if i % 2 ==0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
print(r)

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x,y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x,y in zip(w,f)}
print(d)

s = set()

for i in range(10):
    s.add(i)

print(s)
s = {i for i in range(10) if i % 2 == 0}
print(s)

l = [1,2,3]
i = 5

del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
finally:
    print('clean up')

print("last")

class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')














