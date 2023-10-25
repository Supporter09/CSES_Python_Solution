arr = list(map(int, input().split()))
check = False
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        check = True
        print(arr[i], end=' ')

if check == False:
    print("NONE")