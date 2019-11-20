import unittest
import numpy as np
from methods import Methods
import time
import matplotlib.pyplot as plt
# import timeit


class Timer:

    def __init__(self):
        self.speeds = []
        self.arraySize = []

    def array_builder(self, upperlimit, number):
        self.arraySize.append(number)
        return np.random.randint(1, upperlimit, number)

    def run_timer(self, array, method):
        start = time.process_time()
        method(array)
        end = time.process_time()
        speed = (end - start)
        self.speeds.append(speed)


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
    plt.ylabel('execution Time(ms)')
    plt.xlabel('number of items in List')
    plt.show()
