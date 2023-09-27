def add(*args):
    summ1 = 0
    for n in args:
        summ1 += n
    return summ1


summ = add(9, 19, 29, 49, 58)

print(summ)
