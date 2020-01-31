import unittest
from methods import Methods

from mergesort_alice import quicksort
from merge_sort_improved import sort
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
        test_arr = timeTest.array_builder(limit, i)
        timeTest.run_timer(test_arr, method)

    plt.plot(timeTest.xAxis, timeTest.speeds)


def loop_through_methods_and_show_graph(range1, increments, limit, method_list):
    for m in method_list:
        test_method_and_plot(range1, increments, limit, m)
        #test_Int_number_input(range1, increments, m)
    plt.ylabel('execution Time(ms)')
    plt.xlabel('number of items in List')
    plt.show()


if __name__ == '__main__':
    # stocks = Stocks()
    method_list = [Methods.selection_sort, quicksort, sort, Methods.sortit]
    upperrange = 1000
    increments = 5
    limit = 1000

    loop_through_methods_and_show_graph(
        upperrange, increments, limit, method_list)
    # BLUE>ORANGE>GREEN>RED
