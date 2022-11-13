n = int(input())
n -= 1
numEv = (n - n%2) // 2
numod = (n + n%2) // 2
# print(numEv, numod)
m = (n + 1)*45 + numEv*15 + (numod)*5
print(9 + m//60, m%60)
