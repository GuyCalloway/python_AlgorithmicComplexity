import math
import random
import numpy as np


class Methods:
    def get_first(self, data):
        return data[0]

    def count(self, data):
        counter = 0
        for i in data:
            if i == 5:
                counter += 1
        return counter

    def no_primes(self, data):
        counterV = 0

        def is_prime(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        for i in data:
            if is_prime(i):
                counterV += 1

        return counterV

    def shuffle(self, data):
        shuffled = []
        for i in data:
            index = random.randint(0, len(shuffled))
            shuffled.insert(index, i)
        return shuffled

    def shuffle2(self, data):
        length = len(data)
        for _ in range(1, length):
            index = random.randint(0, (len(data)-1))
            data[0], data[index] = data[index], data[0]
        return data

    def shuffle3(self, data):
        length = len(data)
        arr = np.random.randint(0, length, length)
        for x in range(1, length):
            data[0], data[arr[x]] = data[arr[x]], data[0]
        return data

    def reverse(self, data):
        length = len(data)
        reversed = [None] * length
        for i, element in enumerate(data):
            reversed[(length-1) - i] = element
        return reversed

    def reverse2(self, data):
        reversed = [None] * len(data)
        for i, _ in enumerate(data):
            z = data[(i*-1)-1]
            reversed[i] = z
        return reversed

    def find_duplicates(self, data):
        dictionary_count = {}
        dupes = []

        for x in data:
            if x not in dictionary_count:
                dictionary_count[x] = 1
            else:
                dictionary_count[x] += 1

        for k in dictionary_count.keys():
            if dictionary_count[k] == 2:
                dupes.append(k)
        return dupes

    def find_most_freq_values(self, data):
        count_dictionary = {}

        for x in data:
            if x not in count_dictionary:
                count_dictionary[x] = 1
            else:
                count_dictionary[x] += 1
        mostFreq = []
        v = list(count_dictionary.values())
        f = max(v)
        for x in count_dictionary.keys():
            if count_dictionary[x] == f:
                mostFreq.append(x)
        return mostFreq

    def sortit(self, data):
        for n in range(len(data)):
            for i, x in enumerate(data):
                if i != (len(data) - 1):
                    if x > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
        return data

    def sortit2(self, data):
        for index in range(1, len(data)):
            value = data[index]
            i = index - 1
            while i >= 0:
                if value < data[i]:
                    data[i+1] = data[i]
                    data[i] = value
                    i -= 1
                else:
                    break
        return data

    def sort0n1s(self, data):
        count = 0
        nu = []
        for x in data:
            if x == 0:
                nu.append(0)
                count += 1
        z = len(data) - count
        for _ in range(0, z):
            nu.append(1)
        return nu

    def fibonacci(self, N):
        calco = [0, 1]
        if N > 2:
            for _ in range(2, N):
                calco.append(calco[-1] + calco[-2])
        elif N == 0:
            return []
        elif N == 1:
            return [0]
        return calco

    def mecha_coach(self, name_array):
        def flatten(lists): return [
            item for sublist in lists for item in sublist]
        name_couples = []
        length = len(name_array)
        for i, name in enumerate(name_array):

            for x in range(i, length):
                if name != name_array[x]:
                    name_couples.append([name, name_array[x]])

        num_of_couples = len(name_couples)
        name_pairs = []

        for index, couple in enumerate(name_couples):
            for x in range(index, num_of_couples):
                if not self.find_duplicates(flatten([couple, name_couples[x]])):
                    name_pairs.append([couple, name_couples[x]])
        return name_pairs
