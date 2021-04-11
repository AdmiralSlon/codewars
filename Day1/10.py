def move_zeros(array):
    res = []
    null = 0
    for i in array:
        if (type(i) == bool or i != 0):
            res.append(i)
        else:
            null += 1
    for i in range(0, null):
        res.append(0)
    return res
print (move_zeros([1,2,0,1,0,1,0,3,0,1]))

# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))