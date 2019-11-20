import unittest
import numpy as np
from methods import get_first
import time


class Timer:

    def __init__(self):
        self.speed = []
        self.arraySize = []

    def array_builder(self, number):
        self.arraySize.append(number)
        return np.random.randint(1, 101, number)

    def run_test(self, array, method):
        start = time.process_time()
        method(array)
        end = time.process_time()
        speed = (end - start)*1000000
        self.speed.append(speed)


if __name__ == '__main__':
    timeTest = Timer()
    for i in range(1, 100000, 5000):
        test_list = timeTest.array_builder(i)
        timeTest.run_test(test_list, get_first)
    print(timeTest.speed)
    print(timeTest.arraySize)
