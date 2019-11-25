import numpy as np
import time


class Timer:

    def __init__(self):
        self.speeds = []
        self.xAxis = []

    def array_builder(self, upperlimit, length_list):
        self.setXAxis(length_list)
        return np.random.randint(0, upperlimit, length_list)

    def setXAxis(self, number):
        self.xAxis.append(number)

    def run_timer(self, input, method):
        start = time.process_time()
        method(input)
        end = time.process_time()
        speed = (end - start)
        self.speeds.append(speed)
