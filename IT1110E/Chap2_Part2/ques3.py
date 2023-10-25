n = int(input())

def fibo(n):
    a = (1 + (5**0.5))/2
    b = (1 - (5**0.5))/2
    return (a**n - b**n)//(5**0.5)
print(int(fibo(n)))