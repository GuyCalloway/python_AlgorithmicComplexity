import math
import random
# import numpy


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
        seen = {}
        dupes = []

        for x in data:
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1

        for k in seen.keys():
            if seen[k] == 2:
                dupes.append(k)
        return dupes

    def find_most_freq_values(self, data):
        seen = {}

        for x in data:
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
        mostFreq = []
        v = list(seen.values())
        f = max(v)
        for x in seen.keys():
            if seen[x] == f:
                mostFreq.append(x)
        return mostFreq
