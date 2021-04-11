def order(str):
    if str == '':
        return ''
    i = 0
    tm = ''
    ans = ''
    res = {49:'', 50:'', 51:'', 52:'',53:'', 54:'',55:'', 56:'', 57:''}
    for i in str:
        if i == ' ':
            res[tmnm] = tm
            tm = ''
            continue
        tm += i
        if ord(i) >= 49 and ord(i) <= 57:
            tmnm = ord(i)
    res[tmnm] = tm
    for i in res:
        ans += res[i] + " "
    while True:
        if ans[-1] == " ":
            ans = ans[:-1]
            continue
        break
    return ans
print (order(''))

#def order(sentence):
#    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

#def order(words):
#  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))