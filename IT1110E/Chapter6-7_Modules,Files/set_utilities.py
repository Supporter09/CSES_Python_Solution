def set_union(A,B):
    res = set()
    for el in A:
        res.add(el)
    for el in B: 
        res.add(el)
    return res

def set_intersection(A, B):
    res = set()
    if len(A) >= len(B):
        for el in A:
            if el in B:
                res.add(el)
    else:
        for el in B:
            if el in A:
                res.add(el)
    return res