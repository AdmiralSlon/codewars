def create_phone_number(n):
    return '(' + str(n[0]) + str(n[1]) + str(n[2]) + ') '+str(n[3]) + str(n[4]) + str(n[5]) + '-' + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])


# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# def create_phone_number(n):
#     n = ''.join(map(str,n))
#     return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])