import math


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
        def is_prime(x):
            if x >= 2:
                for y in range(2, int(math.sqrt(x))):
                    if not (x % y):
                        return False
            else:
                return False
            return True
        counter = 0
        for i in data:
            if is_prime(i):
                counter += 1
        return counter
