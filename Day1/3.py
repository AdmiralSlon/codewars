def asdasd(word):
    res = ''
    a = []
    for i in range (0, 200):
        a.append(0)
    str = word
    for s in str:
        a[ord(s)] += 1
    for i in range (97, 122):
        tmp = a[i]
        a[i] += a[i - 32]
        a[i - 32] += tmp
    for s in str:
        if (a[ord(s)] == 1):
            res += '('
        else:
            res += ')'
    return res