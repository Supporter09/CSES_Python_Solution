t = int(input())
for i in range(t):
    y, x = list(map(int, input().split(" ")))

    if (x < y):
        if( y % 2 == 1):
            r = y**2
            print(r - x +1)
        else:
            
