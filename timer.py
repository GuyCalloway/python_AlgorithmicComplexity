import numpy as np
import time


class Timer:

    def __init__(self):
        self.speeds = []
        self.arraySize = []

    def array_builder(self, upperlimit, length_list):
        self.arraySize.append(length_list)
        return np.random.randint(1, upperlimit, length_list)

    def run_timer(self, array, method):
        start = time.process_time()
        method(array)
        end = time.process_time()
        speed = (end - start)
        self.speeds.append(speed)
