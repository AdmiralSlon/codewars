# print(ord('a'))
# def high(x):
#     res = ''
#     tm = ''
#     f = 1
#     mx = 0
#     stm = 0
#     for i in x:
#         if i == ' ':
#             if stm > mx:
#                 res = tm
#                 mx = stm
#             tm = ''
#             stm = 0
#             continue
#         tm += i
#         stm += ord(i) - 96
#     if stm > mx:
#         res = tm
#         mx = stm
#     return res
# print(high('qwe asd xzc'))


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
print (high('max min max min max'))

# def high(x):
#     words=x.split(' ')
#     list = []
#     for i in words:
#         scores = [sum([ord(char) - 96 for char in i])]
#         list.append(scores)
#     return words[list.index(max(list))]