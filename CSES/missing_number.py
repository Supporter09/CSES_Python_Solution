n = int(input())
arr = list(map(int, input().split(" ")))

# Using math 
# Cal sum of n number and - sum of arr
sum_of_n = ((n+1)*n)//2
sum_of_arr = sum(arr)
print(sum_of_n-sum_of_arr)