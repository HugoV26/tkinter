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

l = [1, 2, 3]
#l2 = []
#for v in l:
 #   l2.insert(0, v)
 #print (l2)

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