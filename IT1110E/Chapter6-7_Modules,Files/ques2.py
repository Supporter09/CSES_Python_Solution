import list_utilities
def myfunc(arr):
    check = list_utilities.flatten_nested_list(arr)
    print(*check)
    res = list_utilities.max_num_in_list(check)
    print(res)