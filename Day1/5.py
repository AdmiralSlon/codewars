def get_sum(a,b):
    s = 0
    for i in range(a, b + 1):
        s += i
    a, b = b, a
    for i in range(a, b + 1):
        s += i
    return (a if a == b else s)
print (get_sum(3,0))