import math
def cakes(recipe, available):
    res = 10000000000
    for k in recipe.keys():
        if available.get(k) == None:
            return 0
        res = min(res, available[k] / recipe[k])
    return math.floor(res)

# def cakes(recipe, available):
#     return min(available.get(k, 0)/recipe[k] for k in recipe)