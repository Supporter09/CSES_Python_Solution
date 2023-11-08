def sort_tuple(tup):
    tup = sorted(tup, key = lambda x: float(x[1]), reverse=True)
    return tup

tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort_tuple(tup))