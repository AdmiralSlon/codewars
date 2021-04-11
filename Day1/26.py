from math import e
n = 20
j = 1
res = 1
for i in range(1, n):
    res += 1/(j * i)
    j *= i
print (res)