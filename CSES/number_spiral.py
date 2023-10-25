t = int(input())
for i in range(t):
    y, x = list(map(int, input().split(" ")))

    if (y > x):
        if( y % 2 == 0):
            r = y**2
            print(r - x + 1)
        else:
            r = (y - 1)**2
            print(r + x)
    else:
        if(x % 2 == 0):
            r = (x - 1)**2
            print(r + y)
        else:
            r = x**2
            print(r - y + 1)
