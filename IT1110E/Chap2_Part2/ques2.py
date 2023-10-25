n = int(input())

for i in range(1, 2*n):
    if 1 <= i <= n:
        print(' '*(n-i) + '*'*(2*i-1))
    elif n < i <= 2*n-1:
        print(' '*(i-n) + '*'*(2*(2*n-i)-1))