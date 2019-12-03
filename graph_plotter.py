import unittest
from methods import Methods
from stocks import Stocks
from timer import Timer
import matplotlib.pyplot as plt
# import timeit


def test_Int_number_input(range1, increments, method):
    timeTest = Timer()

    for i in range(1, range1, increments):
        timeTest.setXAxis(i)
        timeTest.run_timer(i, method)

    plt.plot(timeTest.xAxis, timeTest.speeds)


def test_method_and_plot(range1, increments, upperlimit, method):
    timeTest = Timer()

    for i in range(2, range1, increments):
        test_arr = timeTest.array_builder(upperlimit, i)
        timeTest.run_timer(test_arr, method)

    plt.plot(timeTest.xAxis, timeTest.speeds)


def loop_through_methods_and_show_graph(range1, increments, upperlimit, method_list):
    for m in method_list:
        test_method_and_plot(range1, increments, upperlimit, m)
        #test_Int_number_input(range1, increments, m)
    plt.ylabel('execution Time(ms)')
    plt.xlabel('number of items in List')
    plt.show()


if __name__ == '__main__':
    stocks = Stocks()
    methods = Methods()
    method_list = [methods.shuffle2, methods.shuffle3]
    range1 = 100000
    increments = 5000
    upperlimit = 50

    loop_through_methods_and_show_graph(
        range1, increments, upperlimit, method_list)
    # BLUE>ORANGE>GREEN>RED
