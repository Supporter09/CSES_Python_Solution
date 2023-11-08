T = int(input())
while T > 0 :   
    N = int(input())
    arr = list(map(int, input().split()))
    appear_dict = dict()
    for i in range(len(arr)):
        if appear_dict.get(arr[i]) == None:
            appear_dict[arr[i]] = [1, N-i]
        else:
            appear_dict[arr[i]][0] = appear_dict[arr[i]][0] + 1
    
    check_arr = list(map(list, appear_dict.items()))
    check_arr = sorted(check_arr, key = lambda x: (x[1][0], x[1][1]), reverse=True)
    for el in check_arr:
        print((str(el[0]) + ' ')*el[1][0] , end="")
    print()

    T -= 1