def sum_and_count(inp):
    sum_list = []
    cnt_list = []
    for el in inp:
        sum_list.append(sum(el))
        cnt_list.append(len(el))
    return [sum_list, cnt_list]

inp = ((1,2,5), (3,7,5,10), (1,))
sum_list, cnt_list = sum_and_count(inp)
print(*sum_list)
print(*cnt_list)