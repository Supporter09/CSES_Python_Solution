# n = int(input())

# for i in range(n, 0, -1):
#     if i % 2 == 1:
#         print(i, end=' ')


# Bai 2
# n = int(input())
# res = 1

# for i in range(n):
#     res *= i + 1

# print(res)

# Bai 3
# n = int(input())

# res = 0

# for i in range(n):
#     res += 1/(i+1)

# print('%.4f'%res)

# Bai 4
for i in range(100, 1000):
    a = i//100
    b = (i - 100*a)//10
    c = i - 100*a - 10*b

    if(a ** 3 + b ** 3 + c ** 3 == i):
        print(i, end=" ")
