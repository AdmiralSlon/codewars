n = 100000000000000
i = 2
j = 2
tm = 1
while tm + i < n:
    tm += i
    j += 1
    i += len(str(j))
n = n - tm
print(n)
if n == 0:
    print(1)
else:
    i = 1
    cur = 1
    fl = False
    while fl == False:
        for j in str(i):
            if cur == n:
                print(j)
                fl = True
                break
            cur += 1
        i += 1