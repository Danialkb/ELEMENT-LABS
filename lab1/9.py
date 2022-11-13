a, b, c = int(input()), int(input()), int(input())
s = set([a, b, c])
if a != b and b != c and a != c:
    print(0)
else:
    print(3 - len(s) + 1)