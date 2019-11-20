import unittest
import numpy as np
from methods import get_first
import time
import matplotlib.pyplot as plt
#import timeit


class Timer:

    def __init__(self):
        self.speeds = []

    def array_builder(self, number):
        return np.random.randint(1, 101, number)

    def run_test(self, array, method):
        start = time.process_time()
        method(array)
        end = time.process_time()
        speed = (end - start)*1000000
        self.speeds.append(speed)


if __name__ == '__main__':
    timeTest = Timer()
    for i in range(1, 1000000, 5000):
        test_list = timeTest.array_builder(i)
        # get_first is just method taking index 0 of array
        timeTest.run_test(test_list, get_first)
    plt.plot(timeTest.speeds)
    plt.ylabel('executionTime')
    plt.show()
