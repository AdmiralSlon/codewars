def likes(n):
    if len(n) == 0:
        return 'no one likes this'
    elif len(n) == 1:
        return n[0] + ' likes this'
    elif len(n) == 2:
        return n[0] +' and ' + n[1] + ' like this'
    elif len(n) == 3:
        return n[0] + ', ' + n[1] + ' and ' + n[2] + ' like this'
    else:
        return n[0] + ', ' + n[1] + ' and ' + str(len(n) - 2) + ' others like this'
print (likes(['Alex', 'Jacob', 'Mark', 'Max']))
#
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)