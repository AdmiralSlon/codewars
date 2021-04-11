def find_it(seq):
    res = {}
    for i in seq:
        if res.get(i) == None:
            res.setdefault(i, 1)
        else:
            res[i] += 1
    for j in res:
        if res[j] % 2 != 0:
            return j
print (find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i


# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]

