def valid_parentheses(str):
    tm = []
    for i in str:
        if (i == ')' or i == '('):
            if (tm):
                if (i == ')'):
                        if (tm[-1] == '('):
                            tm.pop()
                        else:
                            tm.append(i)
                else: tm.append(i)
            else: tm.append(i)
    return True if (not tm) else False
print(valid_parentheses("(tz(kcrnqr)hadvsodoust(jn()gzd"))

# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False