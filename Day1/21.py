def narcissistic( value ):
    tm = 0
    for i in str(value):
        tm += int(i) ** len(str(value))
    return str(value) + ' is narcissistic' if tm == value else str(value) + ' is not narcissistic'
print (narcissistic(7))


# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))