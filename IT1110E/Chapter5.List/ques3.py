def remove_duplicates(arr):
    check = dict()
    
    for el in arr:
        check[el] = check.get(el, 0) + 1

    res = []
    for key in check:
        if check[key] == 1:
            res.append(key)

    return res

print(remove_duplicates([4, 3, 5, 2, 5, 1, 3, 5]))