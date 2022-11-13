a, b, c = int(input()), int(input()), int(input())
print('NO') if (a >= b + c) or (c >= b + a) or (b >= a + c) else print('YES')