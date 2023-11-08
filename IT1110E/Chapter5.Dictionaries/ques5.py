n = int(input())
a = list(map(int,input().split()))
check_dict = {}
for i in a:
    check_dict[i] = 1
# print(check_dict)
for i in range(1,n):
    for j in range(0,i):
        if(a[j]*a[i] < 0) and (abs(a[i])>abs(a[j])):
            check_dict[a[i]] = max(check_dict[a[i]],check_dict[a[j]]+1)
ans = 1
# print(check_dict)
for i in check_dict.values():
    ans = max(ans,i)
print(ans)
