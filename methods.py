import math
import random


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
        shuffled = [None] * len(data)
        # fixed array here faster to process than adding randomly to empty array
        for i in data:
            index = random.randint(0, (len(shuffled)-1))
            shuffled[index] = i
        return shuffled

    def reverse(self, data):
        length = len(data)
        reversed = [None] * length
        for i, element in enumerate(data):
            reversed[(length-1) - i] = element
        return reversed
