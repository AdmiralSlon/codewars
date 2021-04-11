def is_interesting(number, awesome_phrases):
    f = 2
    for z in range (0,3):
        s = str(number)
        if number < 98:
            return 0
        if number == 99 or number == 98:
            return 1
        kn = 0
        for i in range(1,len(s)):
            if s[i] == '0':
                kn += 1
        if kn == len(s) - 1:
            return f
        rev = s[::-1]
        if rev == s:
            return f
        ks = 0
        for i in range(len(s) - 1):
            if int(s[i])+1 == int(s[i + 1]):
                ks += 1
            if int(s[i]) == 9 and int(s[i + 1]) == 0:
                ks += 1
        if ks == len(s)-1:
            return f
        ks =0
        for i in range(len(s)-1):
            if int(s[i]) == int(s[i + 1]) + 1:
                ks += 1
            if int(s[i]) == 9 and int(s[i + 1]) == 0:
                ks += 1

        if ks == len(s)-1:
            return f
        if awesome_phrases.count(number) > 0:
            return f
        number += 1
        f = 1
    return 0
print (is_interesting(1335, [1337, 256]))