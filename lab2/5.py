a = int(input())
res = 0
i = 0
while a != 0:
    res += (a % 10) * pow(2, i)
    i += 1
    a //= 10
print(res)
