a = int(input())
b = int(input())
x = int(input())
y = int(input())

if (a != x) and (b == y):
    print('YES')
elif (a == x) and (b != y):
    print('YES')
elif (a != x) and (b != y):
    print('NO')


