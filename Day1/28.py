import math
def solve(arr):
    x = sum(arr) - max(arr) - min(arr)
    if max(arr) >= sum(arr) - max(arr):
        return sum(arr) - max(arr)
    else:
        return min(arr) + (x - math.ceil((min(arr) - (max(arr) - x)) / 2))


print(solve([3,3,3]))
