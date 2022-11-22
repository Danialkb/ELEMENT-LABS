def fun(n):
    if n == 0 or n == 1:
        return 1
    return fun(n - 1) + fun(n - 2)


print(fun(int(input())))