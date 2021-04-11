a = [[[]]]
for i in (0,5):
    a.append(i)
for i in (0,5):
    for j in (0,5):
        a.append(i*j)
    for i in (0,5):
        for j in (0,5):
            for l in (0,5):
                a.append(i*j*l)
f = open('zxc.txt', 'wt')
print(f.write(str(a)))
f.close()

