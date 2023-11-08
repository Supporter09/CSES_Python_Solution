n = int(input())

a = []     # mảng để in
par = {}   # mảng phả hệ

for i in range(n - 1):
    x, y = input().split()
    par[x] = y
    a.append(x)   # thêm hết thằng cháu 


root = a[0]
while root in par:   # đi tìm cụ tổ
    root = par[root]
a.append(root)  # nhét cụ tổ vô
a.sort()        # sắp xếp tí in 

for i in a:
    dep = 0
    j = i
    while j in par:
        j = par[j]
        dep += 1
    print(i, dep)