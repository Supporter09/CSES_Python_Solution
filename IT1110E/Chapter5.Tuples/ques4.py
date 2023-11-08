def closest_tuple(tuple_list, query, k):
    k -= 1
    minn = float('inf')
    ans = []
    for i in tuple_list:
        if(minn > abs(i[k]-query[k])):
            minn = abs(i[k]-query[k])
            ans = list(i)
    return tuple(ans)

tuple_list = [(-3, 4, 9), (5, 6, 7), (10, 16, 70), (1, 6, -7)]
query = (1, 2, 5)
k = 3
print(closest_tuple(tuple_list, query, k))