def bubble(ar: list) -> None:
    for i in range(0, len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[i] > ar[j]:
                ar[i], ar[j] = ar[j], ar[i]


a = list(map(int, input().split()))

bubble(a)

print(a)
