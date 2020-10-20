from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        print(f'Function {self.fn.__name__}')
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'The function {self.fn.__name__} worked in {self.finish - self.start}')
        return result

    def fact(n):
        pr = 1
        for i in range(1, n + 1):
            pr *= i
        return pr

    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 1) + fib(n - 2)

fact = Timer(fact)
