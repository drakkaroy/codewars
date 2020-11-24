def cakes(recipe, available):

    if all(elem in list(available.keys()) for elem in list(recipe.keys())):
        calc_list = [((available[elem] // recipe[elem]))
                     for elem in list(recipe.keys())]
        if all([x > 0 for x in calc_list]):
            return min(calc_list)
        else:
            return 0
    else:
        return 0


# cakes({"flour": 500, "sugar": 200, "eggs": 1}, {
#       "flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})

# cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
#       {"sugar": 500, "flour": 2000, "milk": 2000})
