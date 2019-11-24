import unittest
from methods import Methods
from timer import Timer
import matplotlib.pyplot as plt
# import timeit


def test_and_graph(range1, increments, upperlimit, method):
    timeTest = Timer()
    for i in range(1, range1, increments):
        test_list = timeTest.array_builder(upperlimit, i)
        timeTest.run_timer(test_list, method)
    plt.plot(timeTest.arraySize, timeTest.speeds)


if __name__ == '__main__':
    methods = Methods()
    test_and_graph(10000, 50, 150, methods.get_first)  # blue
    test_and_graph(10000, 50, 150, methods.count)  # orange
    test_and_graph(10000, 50, 150, methods.no_primes)  # green
    test_and_graph(10000, 50, 150, methods.shuffle)
    test_and_graph(10000, 50, 150, methods.reverse)  # red
    plt.ylabel('execution Time(ms)')
    plt.xlabel('number of items in List')
    plt.show()
