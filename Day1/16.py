def find_nb(m):
    i = 0
    tm = 0
    while tm < m:
        i += 1
        tm += i ** 3
    return i if tm == m else -1
print(find_nb(1071225))