a, b = map(float, input().split())
tmp = a
if b == 0:
    print(1)
    exit(0)
for i in range(1, int(b)):
    a *= tmp

print(a)