#python aritmatics

a = 8
b = 4

print("these are the data of a and b :", a, b)

print("a+b =", a+b)
print("a*b =", a*b)
print("a/b =", a/b)
print("a**b =", a**b)
print("a%b =", a%b)

print()
#python boolean
# True / False

#python print with endl
print('printing using \"\" =', "hello, world")
print('printing using \'\' =', 'hello, world')

#python print WITHOUT endl
print('printing with end =', 'hello, world', end = ".")
print()
print()
#python to format string
print('format using string :')
print()
print('hello there, my name is {name}'.format(name = 'python'))
print()
print('hello {}, my name is {}'.format('you', 'bambank'))
print()
a = 'hello {name1}, my name is {name2}'.format(name1 = 'you', name2 = 'python')
print(a)

print("input x = ", end = "")
x = input()
print("input y = ", end = "")
y = input()
a = 'hello {name1}, my name is {name2}'.format(name1 = x, name2 = y)
print(a)
print()
a = 'hello ', x, ' my name is ', y
print(a)

print()
#python make a List
print('using list :')
print()
l = [1, 2, 'hello', True, 5.2]
print(l)
l.append('world')
print('l.append "world" =', l)
l.remove(1)
print('l.remove index 1 =', l)
del l[2]
print('del l[index : index] =', l)

print('print l[0] =', l[0])
print()

#python list nesting
print('nest in pyhton :')
nest = [1,2,3,[4,5,['target']]]
print('this is the nest :', nest)
print('nest[0] =', nest[0])
print('nest[3] and in [1] =', nest[3][1])
print('nest [3] and in [2] and in [0] =', nest[3][2][0])

print()
#python dictionary
print('dictionary in python :')
d = {'key1':'item1','key2':'item2'}
print('this is the dictionary :', d)
print('this is the key1 =', d['key1'])

print()
#python tuplets
t = (1,2,3)
print('tuplets in python =')
print('this is the tuplets :', t)
print('tuplets index 0 =', t[0])
#tuplets is unchangeable
print()

#sets 
print('sets in python :')
s = {1,2,3}
print('this is the set =', s)
print()
#sets always do ascending and NO duplication and NO indexing and CANNOT be reverse

s = {1,2,3,1,3,2,1,2,3,2,1}
print(s)
print()
#set can be a list and list can be a set
s = [1,2,3,1,2,3,2,3,1]
print('set of s =', set(s))
print('s still in list form =', s)
s = list(set(s))
print('set changed to list =', s)
print()
#reversing list
s.reverse()
print('s list reversing =', s)
print()

#logical operator
print('logical operator in python :')
print('1 > 2?', 1 > 2)
print('hello = world?', "hello" == "world")

print('(1 < 2) and (2 < 3)?', (1 < 2) and (2 < 3))
print('(1 < 2) & (2 < 3)?', (1 < 2) & (2 < 3))
print()
#if elif and else
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

print()
#python for loop
seq = [1,2,3,4,5]

for item in seq:
    print(item, end = " ")
    
print()
for i in range(6):
    print('hello', end = " ")
    
print()
for i in range(5):
    print(seq[i], end = " ")

print()
for jelly in seq:
    print(jelly+jelly, end = " ")
    
print()
#python While
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
    
#list comprehension
x = [1, 2, 3, 4, 5]

out = []
for item in x:
    out.append(item**2)
print(out)

[item**2 for item in x]
print(x)

#function python
def my_func(param1='default'):
    print(param1)

my_func
my_func()
my_func('new param')
my_func(param1='new param')

def square(x):
    return x**2
out = square(2)
print(out)

#map and filter
seq = [1,2,3,4,5]

def times2(var):
    return var*2

print(map(times2,seq))
print(list(map(times2,seq)))

#lambda = python random function name
print(list(map(lambda var: var*2,seq)))
print(list(filter(lambda item: item%2 == 0,seq)))

#method string
s = 'hello my name is Python'
s = s.lower()
print(s)
s = s.upper()
print(s)
s = s.split()
print(s)

st = 'go go! #hello go'
st = st.split('#')
print(st)

st = 'go go! #hello go'
st = st.split('#')[1]
print(st)

print('x' in ['x', 'y', 'z'])
print(x in [1, 2, 3])
