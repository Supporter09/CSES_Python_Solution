T = int(input())

while T > 0:
    check = True
    # ld is an array where its indices indicate row-col+N-1
    # (N-1) is for shifting the difference to store negative
    # indices
    ld = [0] * 17

    # rd is an array where its indices indicate row+col
    # and used to check whether a queen can be placed on
    # right diagonal or not
    rd = [0] * 17

    # Column array where its indices indicates column and
    # used to check whether a queen can be placed in that
    # row or not
    cl = [0] * 17
    arr = []
    for _ in range(8):
        pair = list(map(int, input().split()))
        arr.append(pair)
    
    for pair in arr:
        x, y = pair
        if ((ld[x - y + 8 - 1] != 1 and rd[x + y] != 1) and cl[x] != 1):

            ld[x - y + 8 - 1] = rd[x + y] = cl[x] = 1
        else:
            check = False
            break

    if check == False:
        print("YES")
    else:
        print("NO")

    T -= 1
