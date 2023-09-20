n = int(input())
arr = list(map(int, input().split(" ")))

map_n = {}

for el in arr:
    if el not in map_n:
        map_n[el] = 1
    else:
        map_n[el] += 1

for key, val in map_n.items():
    print(key, val)
