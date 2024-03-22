""""Practice with Dictionaries and for Loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}
# print out the keys that have true values

for key in in_stock:
    if in_stock[key] is True:
        print(key)