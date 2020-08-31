'''
nums = []
vals = nums[:]
print(vals)
vals.append(1)
print(len(vals))
print(len(nums))

list = [0 for i in range (1, 3)]

print(list)
print(len(list))

print("********")

sara = [0, 1, 2, 3]
x = 1
for elem in sara:
    x *= elem

print(x)

print("********")

print(2 == 2)

print("********")

xa = 1
xa = xa == xa
print(xa)

k = 0
while k <= 3:
    k += 2
    print("*")
'''

#i = 0
#while i <= 5:
 #   i+=1
  #  if i%2 == 0:
   #     break
    #print("*")
'''
for i in range(1):
    print("#")
else:
    print("#")
    '''
'''
var = 0
while var < 6:
    var += 1
    if var%2 == 0:
        continue
    print("#")
'''
'''
var = 1
while var < 10:
    print("#")
    var = var << 1
'''
'''
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)
'''
'''
a = 1
b = 0
c = a&b
d = a|b
e = a^b
print(c+d+e)
'''
'''
l = [3, 1, -2]
print(l[l[-1]])
'''
#l = [1, 2, 3, 4]
#print(l[-3:-2])

#vals = [0, 1, 2]
#vals[0], vals[2] = vals[2], vals[0]

#print(vals)

#vals.insert(0, 1)
#del vals[1]
#print(vals)

#nums = [1, 2, 3]
#vals = nums
#del vals[1:2]

#vals = nums[-1:-2]

#print(len(nums))
#print(len(vals))

#l = [1, 2, 3]
#l2 = []
#for v in l:
 #   l2.insert(0, v)
 #print (l2)

'''
for v in range(len(l)):
    l.insert(1, l[v])

print(l)

lista4 = [i for i in range (-1, 2)]
print(len(lista4))

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s+=t[i][i]
print(s)  

ora = [[0, 1, 2, 3] for i in range(2)]
print(ora[2][0])
'''
'''
t = (1, ) + (1, )
t = t + t
print(len(t))
'''
'''
def sara(x=0):
    return x

print(sara(2))
'''
'''
def sara(x):
    if x == 0:
        return 0
    return x + sara(x-1)

print(sara(3))
'''
'''
def fun(x):
    x += 1
    return x

x = 2
x = fun(x+1)
print(x)
'''
'''
dct = {}
lst = ['a', 'b', 'c', 'd']

for i in range(len(lst) - 1):
    dct[lst[i]] = {lst[i]}
for i in sorted(dct.keys()):
    k = dct[i]
    print(k["0"])
'''

#def sara(a, b):
#    return a ** a

#print(sara(2))
'''
def sara(a):
    return a ** a

def hugo(a):
    return sara(a) * sara(a)

print(hugo(2))'''

'''
def sara(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(sara(sara(2)) + 1)
'''
'''
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)
'''
'''
def any():
    print(var + 1, end='')
var = 1
any()
print(var)'''
'''
t = (1, 2)

t[1] = t[1] + t[0]

print(t[0]) 

'''
'''
sara = ['Hugo', 'Dooku', 'a', 'Title', 'labm']

sara[3] = "weljnfjl"
print(sara)

def myList(sara):
    del sara[3]
    sara[3] = 'ram'

print(myList(sara))'''

'''
def fun(a, b):
    return a + b

print(fun(a = 1, 5))
'''
'''
def fun(inp=2, out=3):
    return inp * out

print(fun(out = 2))
'''


'''
sara = {'one': 'two', 'three': 'one', 'two': 'three'}
v = sara['three']

for k in range(len(sara)):
    v = sara[v]

print(v)
'''
'''
sara = (1, 2, 4 , 8)
sara = sara[1:-1]
sara = sara[0]
print(sara)
'''

'''
sara = [1, 2]

for v in range(2):
    sara.insert(-1, sara[v])

print(sara)
'''
'''
sara = [1, 2, 3]
hugo = sara

print(len(sara))
print(len(hugo))

'''
'''
def sara(a):
    return None

def hugo(a):
    return sara(a) * sara(a)

print(hugo(2))
'''

#print(1//2)

'''
z = 0
y = 10
x = y < z and z > y or y > z and z < y

print(x)
'''
'''
sarahi = [x * x for x in range(5)]

def fun(sara):
    del sara[sara[2]] 
    return sara

print(fun(sarahi))
'''
'''
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
'''
'''
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
'''
'''
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))
'''
'''
nums = [1, 2, 3]
vals = nums

print(nums)
print(vals)


del vals[:]

print(nums)
print(vals)
'''
'''
x = int(input("Valor 1: "))
y = int(input("Valor 2: "))

x = x%y
x = x%y
y = y%x

print(y)

'''

#print("a", "b", "c", sep="sep")

#x = 1 // 5 + 1 / 5
#print(x)

'''
x = float(input("Valor 1: "))
y = float(input("Valor 2: "))

print(y ** (1/x))

'''
'''
sara = {i for i in range(-1, -1)}

print(sara)
print(len(sara))
'''
'''
def sara(a, b, c=0):
    return

sara(a=0, b=1)
'''
'''
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))
'''
'''
i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")
    '''
'''
sara = (1, 2, 4, 8)
sara = sara[-2:-1]
sara = sara[-1]
print(sara)
'''
'''
dd = { "1": "0", "0":"1"}

for x in dd.vals():
    print(x, end ="")
    '''
'''
sara = {}
sara['1'] = (1, 2)
sara['2'] = (2, 1)

for x in sara.keys():
    print(sara[x][1], end = "")
    '''

sara = [[x for x in range(3)] for y in range(3)]

print(sara)

for r in range(3):
    for c in range(3):
        if sara[r][c] % 2 != 0:
            print("#")