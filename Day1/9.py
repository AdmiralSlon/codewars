def sort_array(source_array):
    tm = []
    for i in source_array:
        if i % 2 == 1:
            tm.append(i)
    tm.sort()
    j = 0
    for i in range(0, len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = tm[j]
            j += 1
    return (source_array)
print (sort_array([]))