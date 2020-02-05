import timeit
import functools


def factorial(int):
    tot = 1
    for num in range(int):
        tot *= (int - num)
    return tot


def factorial2(int):
    if int == 1:
        return 1
    return int * factorial2(int-1)


for f in [factorial, factorial2]:
    print('{} takes {} usec/loop'.format(f.__name__,
                                         timeit.timeit(functools.partial(f, 10))))
