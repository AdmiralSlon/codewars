n = '11'
tm = {'0' : '08', '1' : '124', '2' : '1235', '3' : '236', '4' : '1457', '5' : '24568', '6' : '3569', '7' : '478', '8' : '05789', '9' : '689'}
res = ['']
ans = []
tp = 0
for i in n:
    tp += 1
    lt = len(res)
    for j in tm[i]:
        for k in range (0, lt):
            res.append(res[k] + j)
    # for p in res:
    #     if len(p) < tp:
    #         for l in range (0, res.count(p)):
    #             res.remove(p)
for l in res:
    if len(l) == tp:
        ans.append(l)
print (ans)


# def get_pins(observed):
#   map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
#          ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
#   return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]