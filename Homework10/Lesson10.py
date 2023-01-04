def fib(n):
    Limit = n
    count = 0
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        if (count == Limit):
            break
        count += 1
n = int(input("Введите число: "))
num_fib = fib(n)
print(next(num_fib))
print(next(num_fib))
print(next(num_fib))
print(next(num_fib))
print(next(num_fib))


