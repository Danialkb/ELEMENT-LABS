x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())
if x == x1 and y != y1:
    print('YES')
elif x != x1 and y == y1:
    print('YES')
else:
    print('NO')
