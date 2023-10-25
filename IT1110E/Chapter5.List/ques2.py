N = int(input())
arr = list(map(int, input().split()))
x = int(input())

nearest_value = 1005
res = 1005

for i in range(N):
    if abs(arr[i] - x) < nearest_value:
        res = arr[i]
        nearest_value = abs(arr[i] - x)

print(res)
