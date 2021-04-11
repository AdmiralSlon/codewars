def dig_pow(n, p):
    tm = 0
    for i in str(n):
        tm += int(i) ** p
        p += 1
    return int(tm / n) if ((tm / n - int(tm / n)) == 0) else -1
print (dig_pow(46288, 3))