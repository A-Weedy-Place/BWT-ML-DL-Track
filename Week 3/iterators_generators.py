class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        self.num = self.start
        return self
    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        else:
            result = self.num
            self.num -= 1
            return result

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
import random

def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)
        

def main():

    print("Countdown:")
    countdown = Countdown(10)
    for number in countdown:
        print(number)

    print("Fibonacci sequence to 100:")
    for fibo in fibonacci_generator(100):
        print(fibo)

    print("Random nums 1-10:")
    for randum in random_number_generator(1, 10, 5):
        print(randum)

main()