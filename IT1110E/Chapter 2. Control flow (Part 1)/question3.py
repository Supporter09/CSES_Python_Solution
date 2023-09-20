a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral")
elif a == b != c or a == c != b or b == c != a :
    print('Isosceles')
else:
    print('Scalene')
