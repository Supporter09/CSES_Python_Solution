n = int(input())

for i in range(1, n+1):
    a = ''.join([str(x) for x in range(1, i+1)])
    print(' '*(n-i) + a + a[:i-1][::-1] )