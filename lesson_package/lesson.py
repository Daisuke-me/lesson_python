s = 'konnnitiha mike'
print(s)

is_start = s.startswith('k')
print(is_start)

print(s.find('mike'))
print(s.rfind('iti'))

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.replace('mike', 'jon'))
print(s)

r = [1,2,3,4,5,1,2,3]
x = r.index(3,0)
print(x)
if 51 in r:
    print('exist')

r.sort()
print(r)

i = [1,2,3,4,5]
j = i
j[0] = 100
print(i)
print(j)

x = [1,2,3,4,5]
y = x[:]
y[0] = 100
print(x)
print(y)

x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print(x)
print(y)

c = 20
d = c
d = 5
print(c)
print(d)

num_tuple = (10,20)
print(num_tuple)

x,y = num_tuple
print(x)
print(y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
i, j = j, i
print(i,j)

chose_from_two = ('A','B','C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

fruit = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruit['apple'])

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'F','G'}
print(my_friends & A_friends)































