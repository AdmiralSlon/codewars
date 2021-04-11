def accum(s):
    res = ''
    j = 0
    str = s.lower()
    for i in str:
        res += i.upper() + i * j + '-'
        j += 1
    res = res[:-1]
    return (res)

print (accum('asd'))