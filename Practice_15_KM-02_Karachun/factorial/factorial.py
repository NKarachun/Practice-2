def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x
