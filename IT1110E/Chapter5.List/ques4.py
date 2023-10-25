N, K = map(int, input().split())
row = 'I'*N

for _ in range(K):
    l, r = map(int, input().split())
    a = row[:l-1] 
    b = row[r:]
    row = a + '.'*(r-l+1) + b

print(row)