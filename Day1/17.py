def find_outlier(integ):
    nch, ch, nchm, chm  = 0, 0, 0, 0
    for i in integ:
        if i % 2 != 0:
            nch = i
            nchm += 1
        else:
            ch = i
            chm += 1
    return ch if chm == 1 else nch


# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]