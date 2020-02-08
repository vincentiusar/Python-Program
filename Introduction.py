#python aritmatics

a = 8
b = 4

print("these are the data of a and b :", a, b)

print("a+b =", a+b)
print("a*b =", a*b)
print("a/b =", a/b)
print("a**b =", a**b)
print("a%b =", a%b)

#python boolean
# True / False

#python print with endl
print("hello, world")
print('hello, world')

#python print WITHOUT endl
print('hello, world', end = ".")

#python to format string
print('hello there, my name is {name}'.format(name = 'python'))

print('hello {}, my name is {}'.format('you', 'bambank'))
a = 'hello {name1}, my name is {name2)'.format(name1 = 'you', name2 = 'python')
print(a)

print("input x =", end = "")
x = input()
print("input y =", end = "")
y = input()
a = 'hello {name1}, my name is {name2}'.format(name1 = x, name2 = y)
print(a)

a = 'hello ', x, ' my name is ', y
print(a)

#python make a List
l = [1, 2, 'hello', True, 5.2]
l.append('world')
print(l)
l.remove(1)
print(l)
del l[2]
print(l)

print(l[0])

#python list nesting
nest = [1,2,3,[4,5,['target']]]
print(nest[0])
print(nest[3][1])
print(nest[3][2][0])

#python dictionary
d = {'key1':'item1','key2':'item2'}
print(d['key1'])

#python tuplets
t = (1,2,3)
print(t[0])
#tuplets is unchangeable

#sets 
s = {1,2,3}
print(s)

#sets always do ascending and NO duplication and NO indexing and CANNOT be reverse

s = {1,2,3,1,3,2,1,2,3,2,1}
print(s)

#set can be a list and list can be a set
s = [1,2,3,1,2,3,2,3,1]
print(set(s))
print(s)
s = list(set(s))
print(s)

#reversing list
s.reverse()
print(s)

#logical operator
print(1 > 2)
print("hello" == "world")

print((1 < 2) and (2 < 3))
print((1 < 2) & (2 < 3))

#if elif and else
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
