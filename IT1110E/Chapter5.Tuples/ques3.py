def tup2num(tup):
    res = ''
    for el in tup: res += str(el)
    return int(res)

tup = (1, 23, 567)
print(tup2num(tup))