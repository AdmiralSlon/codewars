import math
def zxc(inp):
    inp = float(inp)
    if inp == 0:
        return 'круговая орбита'
    elif inp > 0 and inp < 1:
        return 'эллиптическая орбита'
    elif inp == 1:
        return 'параболическая орбита'
    elif inp > 1 and inp < math.inf:
        return 'параболическая орбита'
    elif inp == math.inf:
        return 'прямая'
    else:
        return 'неверные данные'
while True:
    print(zxc(input()))